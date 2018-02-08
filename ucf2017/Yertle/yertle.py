class Pyramid:
	def __init__(self,turtleStrengths,globalWeight):
		self.strengths = sorted(turtleStrengths)
		self.globalWeight = globalWeight
		self.container = []
		self.maxHeight = self.constructPyramid()


	def constructPyramid(self):
		self.container.append([Turtle(self,root=True)])
		previousRowNum = 0
		while True:
			row = []
			parentTurtles = self.container[previousRowNum]
			prevRowCount = len(parentTurtles)
			currentRowCount = prevRowCount + 1
			for pos in range(currentRowCount):
				if 0 < pos < (currentRowCount - 1):
					firstParent = parentTurtles[pos - 1]
					secondParent = parentTurtles[pos]
					newTurtle = Turtle(self, [firstParent,secondParent])
					if newTurtle.strength == False:
						break
					else:
						row.append(newTurtle)
				if pos == 0:
					firstParent = parentTurtles[pos]
					newTurtle = Turtle(self,[firstParent])
					if newTurtle.strength == False:
						break
					else:
						row.append(newTurtle)
				if pos == (currentRowCount - 1):
					firstParent = parentTurtles[pos - 1]
					newTurtle = Turtle(self,[firstParent])
					if newTurtle.strength == False:
						break
					else:
						row.append(newTurtle)
			if len(row) < currentRowCount:
				return prevRowCount
			else:
				self.container.append(row)
				previousRowNum += 1

class Turtle:
	def __init__(self,pyramid,parents=[],root=False):
		self.pyramid = pyramid
		self.parents = parents
		self.weight = pyramid.globalWeight
		self.strengths = pyramid.strengths
		self.threshold = self.getThreshold()
		if root:
			self.strength = 0
		else:
			self.strength = self.getOptimalTurtle()

	def getThreshold(self):
		thres = 0
		for parent in self.parents:
			thres += parent.threshold / 2
			thres += parent.weight / 2
		return thres

	def getOptimalTurtle(self):
		for pos,strength in enumerate(self.pyramid.strengths):
			if strength >= self.threshold:
				self.pyramid.strengths.pop(pos)
				return strength
		else:
			return False

	def __repr__(self):
		return str(self.strength)


with open('input.txt') as f:
	numOfPonds = int(f.readline())
	for i in range(numOfPonds):
		numOfTurtles, weight= [int(data) for data in f.readline().strip().split()]
		turtleStrengths = [int(w) for w in f.readline().strip().split()]
		pyramid = Pyramid(turtleStrengths, weight)
		print(pyramid.container,pyramid.maxHeight)





