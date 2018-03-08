class Wood:
	def __init__(self,length,remainingCuts):
		self.length = length
		self.remainingCuts = remainingCuts
		self.sequence = []
		self.children = [{'start':0,'end':self.length}]
		self.currentCost = 0

	def cut(self,cutPos):
		for pos,child in enumerate(self.children):
			start = child['start']
			end = child['end']
			if start < cutPos < end:
				self.sequence.append(cutPos)
				self.remainingCuts.remove(cutPos)
				self.currentCost += abs(end - start)
				self.children.pop(pos)
				for newChild in self.generateNewChildren(start,end,cutPos):
					self.children.append(newChild)
				break
		else:
			raise Exception('No viable cut was found')

	def generateNewChildren(self,start,end,pos):
		childOne = {'start':start,'end':pos}
		childTwo = {'start':pos,'end':end}
		return [childOne,childTwo]




import copy
cache = {}

def main(length,cuts):
	wood = Wood(length,cuts)
	remainingCuts = cuts
	currentSequence = ''
	cache[''] = wood
	recursion(currentSequence,remainingCuts)
	minimum = None
	for key in cache:
		wood = cache[key]
		if minimum == None and len(wood.sequence) == len(cuts):
			minimum = wood
		elif len(wood.sequence) == len(cuts) and wood.currentCost < minimum.currentCost:
			minimum = wood
	print(minimum.currentCost,minimum.sequence)

def recursion(currentSequence,remainingCuts):
	#print(currentSequence)
	if currentSequence not in cache:
		#Checks if the current sequence has been stored in cache
		newWood = copy.deepcopy(cache[currentSequence[0:-1]])
		#Copies Value of previous parent sequence
		newWood.cut(int(currentSequence[-1]))
		#Cuts the parent sequence at last previous cut that wasn't recorded
		cache[currentSequence] = newWood
		#Adds sequence to cache
	for pos,cut in enumerate(remainingCuts):
		newCuts = copy.copy(remainingCuts)
		newCuts.pop(pos)
		#Gets the new remaining cuts
		recursion(currentSequence + str(cut),newCuts)
	return



main(20,[1,2,3,4,5,6,7,8])