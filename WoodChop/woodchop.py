# def memoize(func):
# 	cache = func.cache = {}
# 	def wrapper(*args):
# 		key = str(args)
# 		if key not in cache:
# 			newCost = cost + 0
# 			cache[key] = {value:func(*args),cost:newCost}
# 		return cache[key]
# 	return wrapper

# @memoize
# def woodCutter(length,*args):

# 	return length,args

# def main(length,cuts):
# 	#Initialize first cuts
# 	for cut in cuts:
# 		woodCutter(cut)
# 	#Loop through every
# 	while True:
# 		cache = woodCutter.cache
# 		for key in cache:


#Solution 1

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
def recursion(wood):
	stack = [wood]
	while True:
		wood = stack.pop(0)
		if len(wood.remainingCuts) == 0:
			break
		for cutPos in wood.remainingCuts:
			newWood = copy.deepcopy(wood)
			newWood.cut(cutPos)
			stack.append(newWood)
	minAmountPile = stack[0]
	for woodPile in stack:
		if woodPile.currentCost < minAmountPile.currentCost:
			minAmountPile = woodPile
	return minAmountPile

wood = Wood(10,[1,5,6,7,9])
found = (recursion(wood))
print(found.sequence,found.currentCost)