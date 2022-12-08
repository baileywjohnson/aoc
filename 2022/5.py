import re

with open('5.txt') as f:

    cargo = {
        1: ['N', 'R', 'G', 'P'],
        2: ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
        3: ['M', 'S', 'V'],
        4: ['L', 'S', 'R', 'C', 'Z', 'P'],
        5: ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
        6: ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
        7: ['H', 'D', 'G', 'W', 'P'],
        8: ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
        9: ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
    }

    for line in f.readlines():

        _line = line.strip()
        sft = [int(s) for s in re.findall(r'\d+', _line)]
        slice_size, from_spot, to_spot = sft[0], sft[1], sft[2]

        _slice = cargo[from_spot][len(cargo[from_spot]) - slice_size:]
    
        cargo[from_spot] = cargo[from_spot][0:len(cargo[from_spot]) - slice_size]

        # Uncomment for Solution to Part I
        # _slice.reverse()

        cargo[to_spot] = cargo[to_spot] + _slice

    output = ""
    for stack in cargo.values():
        output += stack[-1]
    print(output)