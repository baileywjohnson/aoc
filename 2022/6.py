with open('6.txt') as f:
    input = f.read()
    start, end = 0, 13
    chars = set(input[start:end + 1])
    while len(chars) != 14:
        start += 1
        end += 1
        chars = set(input[start:end + 1])
    print(end + 1)