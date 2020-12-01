txt = open("input.txt").read().split()

for i in range(len(txt)):
    for j in range(i):
        x = int(txt[i])
        y = int(txt[j])
        if x + y == 2020: print(x * y)