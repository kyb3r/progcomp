import copy
import math

def encode(fourDigitNumber):
	count = 0
	r = 0
	for digit in fourDigitNumber:
		digit = int(digit)
		d = (3 * digit + 7) % 10
		r += (2**(3*d+2)) + (count*(8**d))
		count += 1
	return r


def matcher(codeOne,codeTwo):
	bulls = ""
	cows = ""
	for pos in range(10):
		p = codeOne/(8**pos)%8
		q = codeTwo/(8**pos)%8
		r = p-q
		s = 2*r + 3*q
		if s > 11 and s > 2 * r:
			if s == 3*p:
				bulls += ('B')
			else:
				cows += ('C')
	return bulls+cows

def generateDigitValues(numOfDigits=4):
	numbers = ['']
	for i in range(numOfDigits):
		newNumbers = []
		for number in numbers:
			for digit in range(10):
				if str(digit) in number:
					continue
				else:
					newNumbers.append(str(number) + str(digit))
		numbers = newNumbers

	return numbers

def selectMiddleNumber(possibilities):
	length = len(possibilities)
	midPoint = length/2
	if midPoint % 2 == 0:
		#Returns largest of midpoint values from list
		return possibilities[int(midPoint)]
	else:
		#Returns midpoint value from list
		return possibilities[int(math.ceil(midPoint)) - 1]

def findSimilarity(given, second):
	if len(given) != len(second):
		return false
	count = 0
	for pos,char in enumerate(given):
		if char == second[pos]:
			count += 1
	return count

def filterList(guess,result,possibilities):
	necessaryDigits = list(guess)
	cows = result.count('C')
	bulls = result.count('B')
	possibilities = filterCows(guess,cows + bulls,possibilities)
	possibilities = filterBulls(guess,bulls,possibilities)
	return possibilities
def filterBulls(guess,bulls,possibilities):
	newPossibilites = []
	for possibility in possibilities:
		similarity = findSimilarity(guess,possibility)
		if similarity != bulls:
			pass
		else:
			newPossibilites.append(possibility)

	return newPossibilites

def filterCows(guess,cows,possibilities):
	newPossibilites = []
	for possibility in possibilities:
		digitCount = 0
		for digit in possibility:
			if digit in guess:
				digitCount += 1
		if digitCount == cows:
			newPossibilites.append(possibility)

	return newPossibilites


def guessSecretNumber(secretNumber):
	possibilities = generateDigitValues()
	allowedDigits = {}
	while True:
		if len(possibilities) == 1:
			print(possibilities)
			break
		guess = (selectMiddleNumber(possibilities))
		result = (matcher(encode(guess),secretNumber))
		possibilities = filterList(guess,result,possibilities)



secretNumber = 83916806
guessSecretNumber(secretNumber)

