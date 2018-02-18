import copy

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
	for pos in range(0,10):
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

def generateDigitValues(digits):
	numbers = [[]]
	for i in range(digits):
		newNumbers = []
		for number in numbers:
			for digit in range(10):
				if digit in number:
					continue
				else:
					newNumber = copy.deepcopy(number)
					newNumber.append(digit)
					newNumbers.append(newNumber)
		numbers = newNumbers
	return numbers

def guessSecretNumber(secretNumber):
	possibilities = generateDigitValues(4)
	print(len(possibilities))

guessSecretNumber(4)

print(encode('1234'))

print(matcher(620781575,encode('7094')))

