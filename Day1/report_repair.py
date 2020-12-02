txt = open("input.txt").read().split()

# Part 1
for i in range(len(txt)):
    for j in range(i):
        x = int(txt[i])
        y = int(txt[j])
        if x + y == 2020: print(x * y)

# Part 2
for i in range(len(txt)):
    for j in range(i):
        for k in  range(j):
            x = int(txt[i])
            y = int(txt[j])
            z = int(txt[k])
            if x + y + z == 2020: print(x * y * z)