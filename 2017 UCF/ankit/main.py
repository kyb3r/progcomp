with open('input.txt') as f:
    num_of_numbers = int(f.readline())
    for _ in range(num_of_numbers):

        number = [int(i) for i in f.readline().strip()]

        properties = set()

        for digit in number:
            if digit == 0:
                properties.add('ninjas')
            if len(str(digit*2)) > 1:
                properties.add('pirates')
            if digit == 1:
                properties.add('knights')
        
        print(''.join(str(i) for i in number), ' '.join(properties))