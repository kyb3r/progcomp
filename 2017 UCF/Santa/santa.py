from collections import Counter

def getHouses(starting,frequency,count,maxHouses):
	visited = []
	currentHouse = starting
	for i in range(count):
		visited.append(currentHouse)
		currentHouse += frequency
		if currentHouse > maxHouses:
			break
	return visited

with open('input.txt') as f:
	years = int(f.readline().strip())
	for i in range(years):
		currentRecord = Counter()
		maxHouses, days = [int(i) for i in f.readline().strip().split()]
		print(maxHouses,days)
		for j in range(days):
			starting, frequency, count = [int(i) for i in f.readline().strip().split()]
			print(starting,frequency,count)
			houses = getHouses(starting,frequency,count,maxHouses)
			for house in houses:
				currentRecord[house] += 1
		print(currentRecord.most_common())




