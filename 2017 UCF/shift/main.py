with open('input.txt') as f:
    sentences = int(f.readline())
    shiftKeys = list('~!@#$%^&*()_+{}|:"<>')
    for i in range(sentences):
        sentence = list(f.readline().strip())
        shift = ''
        for char in sentence:
            if char in shiftKeys or char.isupper():
                shift += '1'
            else:
                shift += '0'
        
        print(len(shift.split('0')))
