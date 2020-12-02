txt = open("input.txt").read().splitlines()

# Part 1
num_valid_pass = 0
for line in txt:
    parts = line.split()
    lim = [int(n) for n in parts[0].split('-')]
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if lim[0] <= wrd.count(ltr) <= lim[1]:
        num_valid_pass += 1   
print(num_valid_pass)

# Part 2
num_valid_pass = 0
for line in txt:
    parts = line.split()
    lim = [int(n) for n in parts[0].split('-')]
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if (wrd[lim[0]-1] == ltr) ^ (wrd[lim[1]-1] == ltr):
        num_valid_pass += 1   
print(num_valid_pass)

# Alternatives:

#     cmin = line.split('-')[0]
#     cmax = line.split('-')[1].split()[0]
#     lttr = line.split('-')[1].split()[1].strip(':')
#     word = line.split('-')[1].split()[2]

#     line1 = line.split('-')
#     line2 = line1[1].split()
#     cmin = line1[0]
#     cmax = line2[0]
#     lttr = line2[1].strip(':')
#     word = line2[2]