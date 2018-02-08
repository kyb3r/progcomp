


def find_shoe_size(first, second):
    size = first + 1
    if abs(second - size) > 1:
        return False # the first shoe fits
    return True # both shoes fit


with open('input.txt') as f:
    num_litters = int(f.readline())
    for _ in range(num_litters):
        seahorses = int(f.readline())
        sizes = [int(i) for i in f.readline().split()]
        sizes.sort()
        pairs = 0
        while True:
            if not sizes: break
            first = sizes.pop(0)
            if not sizes:
                pairs += 1
                break
            second = sizes.pop(0)
            if not find_shoe_size(first, second):
                sizes.insert(0, second)
            pairs += 1
        print(sizes)
        print(pairs)



