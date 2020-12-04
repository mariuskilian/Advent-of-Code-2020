input = open("Day1/input.txt").read().split()

# Part 1
for i in range(len(input)):
    for j in range(i):
        x = int(input[i])
        y = int(input[j])
        if x + y == 2020: print(x * y)

# Part 2
for i in range(len(input)):
    for j in range(i):
        for k in  range(j):
            x = int(input[i])
            y = int(input[j])
            z = int(input[k])
            if x + y + z == 2020: print(x * y * z)

# Combined solution
for i in range(len(input)):
    x = int(input[i])
    for j in range(i):
        y = int(input[j])
        if x + y == 2020: print("Part 1 solution: " + str(x * y))
        for k in  range(j):
            z = int(input[k])
            if x + y + z == 2020: print("Part 2 solution: " + str(x * y * z))
