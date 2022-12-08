with open('2.txt') as f:
    total_score = 0
    for line in f.readlines():
        # Round
        round_score = 0
        chars = line.split()
        i, j = chars[0], chars[1]
        # You Lose
        if j == 'X':
            round_score += 0
            if i == 'A':
                round_score += 3
            elif i == 'B':
                round_score += 1
            else:
                round_score += 2
        # You Tie
        elif j == 'Y':
            round_score += 3
            if i == 'B':
                round_score += 2
            elif i == 'A':
                round_score += 1
            else:
                round_score += 3
        # You Win
        else:
            round_score += 6
            if i == 'C':
                round_score += 1
            elif i == 'A':
                round_score += 2
            else:
                round_score += 3

        total_score += round_score

    print(total_score)