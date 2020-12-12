input = open("Day5/input.txt").read()
boarding_passes = input.splitlines()

# Naive solution
# Part 1
max_seat_id = -1
for bp in boarding_passes:
    row = [0, 127]
    for c in bp[:7]:
        half = (row[0] + row[1]) // 2
        if c == 'F': row[1] = half
        else: row[0] = half + 1
    column = [0, 7]
    for c in bp[7:]:
        half = int(column[0] + column[1]) // 2
        if c == 'L': column[1] = half
        else: column[0] = half + 1
    seat_id = row[0] * 8 + column[0]
    max_seat_id = seat_id if seat_id > max_seat_id else max_seat_id
print(max_seat_id)

#Part 2 
def bp_2_sid(bp):
    row = [0, 127]
    for c in bp[:7]:
        half = (row[0] + row[1]) // 2
        if c == 'F': row[1] = half
        else: row[0] = half + 1
    column = [0, 7]
    for c in bp[7:]:
        half = (column[0] + column[1]) // 2
        if c == 'L': column[1] = half
        else: column[0] = half + 1
    return row[0] * 8 + column[0]
sids = sorted([bp_2_sid(bp) for bp in boarding_passes])
for i in range(1, len(sids)):
    if (sids[i-1]+2 == sids[i]): print(sids[i]-1)

# Combined solution
sids = sorted([bp_2_sid(bp) for bp in boarding_passes])
part1 = sids[len(sids)-1]
for i in range(1, len(sids)):
    if (sids[i-1]+2 == sids[i]): part2 = sids[i]-1
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))

# Advanced solution
# Part 1
print(max([int(''.join(['1' if c in 'RB' else '0' for c in bp]), 2) for bp in boarding_passes]))

# Part 2
sids = sorted([int(''.join(['1' if c in 'RB' else '0' for c in bp]), 2) for bp in boarding_passes])
for i in range(1, len(sids)): print(sids[i]-1) if sids[i-1]+2 == sids[i] else []

# Combined solution
sids = sorted([int(''.join(['1' if c in 'RB' else '0' for c in bp]), 2) for bp in boarding_passes])
part1 = sids[len(sids)-1]
part2 = [x for x in [sids[i]-1 if sids[i-1]+2 == sids[i] else [] for i in range(1, len(sids))] if x][0]
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))