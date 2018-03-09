from math import *

def getNextPoint(currentPoint,points,originLine):
	"""
	Loops through all points and checks which point has smallest angle from origin line to currentpoint
	"""
	minAngle = None
	minAnglePoint = None
	for point in points:
		if point == currentPoint:
			continue
		angle = getAngleToPoint(currentPoint,point,originLine)
		if minAngle == None:
			minAnglePoint = point
			minAngle = angle
		elif angle < minAngle:
			minAnglePoint = point
			minAngle = angle
	return minAnglePoint,minAngle

def getAngleToPoint(currentPoint,checkPoint,originLine):
	"""
	Gets angle 
	Uses cos formula
	"""
	x1,y1 = currentPoint
	x2,y2 = checkPoint
	X = x2 - x1
	Y = y2 - y1
	angle = atan2(Y,X)
	angle = (originLine - angle)
	return angle

def findLeftMostPoint(points):
	"""
	Returns the point with the lowest x value
	"""
	leftMost = points[0]
	for point in points:
		if point[0] < leftMost[0]:
			leftMost = point
	return leftMost

def areaCalc(points):
	print(points)
	total = 0
	for i in range(len(points)-1):
		total += (points[i][0]*points[i+1][1] - points[i+1][0]*points[i][1])
	area = abs(total)/2
	return area


points = []
with open('input.txt') as f:
	for line in f:
		point = [float(i) for i in line.split()]
		points.append(point)

leftMost = findLeftMostPoint(points)
currentPoint = leftMost
connections = []
originLine = pi/2 #90 degree line
count = 0
while True:
	print('Current Point:',currentPoint)
	connections.append(currentPoint)
	currentPoint,minAngle = getNextPoint(currentPoint,points,originLine)
	originLine -= minAngle
	if currentPoint == connections[0] or count > 5:
		break
	else:
		count += 1

print(connections)
print(areaCalc(connections))
