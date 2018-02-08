def shuffle(numOfCards,iterations,permutation):
    deck = list(range(1, numOfCards+1))
    for i in range(iterations):
        newDeck = []
        for pos in permutation:
            newDeck.append(deck[pos-1])
        deck = newDeck
    return deck


with open('input.txt') as f:
    sprees = int(f.readline())
    for i in range(sprees):
        numOfCards,iterations = [int(data) for data in f.readline().split()]
        permutation = [int(data) for data in f.readline().split()]
        deck = shuffle(numOfCards,iterations,permutation)
        print(' '.join(str(i) for i in deck))


