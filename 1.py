with open('1.txt') as f:
    top_three = [float('-inf'), float('-inf'), float('-inf')]
    cur_sum = 0
    for line in f.readlines():
        if line != '\n':
            cur_sum += int(line)
        else:
            if cur_sum > min(top_three):
                top_three[min(range(len(top_three)), key=top_three.__getitem__)] = cur_sum
            cur_sum = 0
    print(sum(top_three))