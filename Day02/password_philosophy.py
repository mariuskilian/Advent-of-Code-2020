input = open("Day2/input.txt").read().splitlines()

# Part 1
num_valid_pass = 0
for line in input:
    parts = line.split()
    lim = [int(n) for n in parts[0].split('-')]
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if lim[0] <= wrd.count(ltr) <= lim[1]:
        num_valid_pass += 1   
print(num_valid_pass)

# Part 2
num_valid_pass = 0
for line in input:
    parts = line.split()
    lim = [int(n) for n in parts[0].split('-')]
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if (wrd[lim[0]-1] == ltr) ^ (wrd[lim[1]-1] == ltr):
        num_valid_pass += 1   
print(num_valid_pass)

# Combined solution
part_1 = 0
part_2 = 0
for line in input:
    parts = line.split()
    lim = [int(n) for n in parts[0].split('-')]
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if lim[0] <= wrd.count(ltr) <= lim[1]: part_1 += 1
    if (wrd[lim[0]-1] == ltr) ^ (wrd[lim[1]-1] == ltr): part_2 += 1
print("Part 1 solution: " + str(part_1))
print("Part 2 solution: " + str(part_2))