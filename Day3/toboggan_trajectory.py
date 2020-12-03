track = open("Day3/input.txt").read().splitlines()

# Part 1
num_trees = 0
slope = 0
for row in track:
    if row[slope] == '#': num_trees += 1
    slope = (slope + 3) % len(row)
print(num_trees)

# Part 2
def slide(slope):
    num_trees = 0
    x_pos = 0
    for i in range(0, len(track), slope[1]):
        if track[i][x_pos] == '#': num_trees += 1
        x_pos = (x_pos + slope[0]) % len(track[i])
    return num_trees
print(slide([1, 1]) * slide([3, 1]) * slide([5, 1]) * slide([7, 1]) * slide([1, 2]))

# Combined solution
part1 = slide([3, 1])
part2 = slide([1, 1]) * slide([3, 1]) * slide([5, 1]) * slide([7, 1]) * slide([1, 2])
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))