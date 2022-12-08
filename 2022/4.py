with open('4.txt') as f:
    total = 0
    for line in f.readlines():
        start_one, start_two = 0, 0
        end_one, end_two = 0, 0

        first = True
        for interval in line.strip().split(','):
            interval_split = interval.split('-')
            if first:
                start_one, end_one = int(interval_split[0]), int(interval_split[1])
                first = False
            else:
                start_two, end_two = int(interval_split[0]), int(interval_split[1])
        
        # Comparisons
        if start_one == start_two or end_one == end_two or start_one == end_two or start_two == end_one:
            total += 1
        elif start_one < end_two and start_two < end_one:
            total += 1
    print(total)