
# with open("3.txt") as f:
#     total = 0
#     for line in f.readlines():
#         items = line.strip()
#         check_unique = set(items[0:len(items)//2])
#         for i in range(len(items)//2, len(items)):
#             if items[i] in check_unique:
#                 if items[i].isupper():
#                     total += ord(items[i].lower()) - 70
#                 else:
#                     total += ord(items[i]) - 96
#                 break
#     print(total)

with open("3.txt") as f:
    total, index = 0, 0
    set_a, set_b, set_c = None, None, None
    for line in f.readlines():
        if index == 0:
            set_a = set(line.strip())
            index += 1
        elif index == 1:
            set_b = set(line.strip())
            index += 1
        else:
            set_c = set(line.strip())
            badge = list(set_a & set_b & set_c)[0]
            if badge.isupper():
                total += ord(badge.lower()) - 70
            else:
                total += ord(badge) - 96
            index = 0
    print(total)
