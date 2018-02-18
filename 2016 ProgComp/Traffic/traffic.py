import copy
def moveCars(road,current,other,empty):
	skip = False
	orginalRoad = copy.deepcopy(road)
	for r,value in enumerate(road):
		if skip:
			skip = False
			continue
		elif value == empty or value == other:
			continue
		elif r == len(roadOne) - 1:
			nextVal = orginalRoad[0]
			if nextVal == empty:
				road[0] = current
				road[r] = empty
		else:
			nextVal = orginalRoad[r+1]
			if nextVal == empty:
				road[r+1] = current
				road[r] = empty
				skip = True
	return road

def checkIntersection(currentRoad,otherRoad,intersection):
	currentIntersection = currentRoad[intersection]
	otherRoad[intersection] = currentIntersection
	return currentRoad,otherRoad

def iterate(roadOne,roadTwo,iterations,intersection):
	for i in range(iterations):
		current = 'R'
		other = 'B'
		empty = '.'
		roadOne = moveCars(roadOne,current,other,empty)
		roadOne,roadTwo = checkIntersection(roadOne,roadTwo,intersection)
		current = 'B'
		other = 'R'
		empty = '.'
		roadTwo = moveCars(roadTwo,current,other,empty)
		roadTwo,roadOne = checkIntersection(roadTwo,roadOne,intersection)
	return (roadOne,roadTwo)

with open('input.txt') as f:
	armSize, iterations = [int(data) for data in f.readline().split()]
	roadOne = list(f.readline().strip())
	roadTwo = list(f.readline().strip())
	print(roadOne,roadTwo)
	intersection = armSize
	print(iterate(roadOne,roadTwo,iterations,intersection))

