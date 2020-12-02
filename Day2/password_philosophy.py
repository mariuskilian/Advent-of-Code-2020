txt = open("input.txt").read().splitlines()

# Part 1
num_valid_pass = 0
for line in txt:
    parts = line.split()
    lim = list(map(int, parts[0].split('-')))
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if lim[0] <= wrd.count(ltr) <= lim[1]:
        num_valid_pass += 1   
print(num_valid_pass)

# Part 2
num_valid_pass = 0
for line in txt:
    parts = line.split()
    lim = list(map(int, parts[0].split('-')))
    ltr = parts[1].strip(':')
    wrd = parts[2]
    if (wrd[lim[0]-1] == ltr) ^ (wrd[lim[1]-1] == ltr):
        num_valid_pass += 1   
print(num_valid_pass)