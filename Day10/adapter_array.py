input = open("Day10/input.txt").read().splitlines()

adapters = sorted([int(i) for i in input])

# Part 1
diff_dist = [0, 0, 1]
diff_dist[adapters[0] - 1] += 1
for i in range(1, len(adapters)): diff_dist[adapters[i] - adapters[i-1] - 1] += 1
print(diff_dist[0] * diff_dist[2])

# Part 2
# 1st Step: Function will find number of arrangements in a given list
def num_arrangements(adapters, idx = 0):
    if idx == len(adapters) - 1: return 1
    max_range = min(len(adapters)-idx-1, 3)
    count = 0
    for i in range(max_range):
        if adapters[idx+i+1] - adapters[idx] > 3: break
        count += num_arrangements(adapters, idx+i+1)
    return count

# 2nd Step: Split adapters whenever there is only one option for the next adapter (`print(a)` to see)
adapters_split = []
a = [0] + adapters + [max(adapters) + 3]
split_offset = 0
for i in range(1, len(a)-1):
    if a[i+1] - a[i-1] > 3:
        adapters_split += [a[split_offset : i+1]]
        split_offset = i

# 3rd Step: Count each split adapter list, then multiply them together
arrangements_cnt = 1
for a in adapters_split: arrangements_cnt *= num_arrangements(a)

print(arrangements_cnt)

# Combined solution:
# Parts are too different - no combined solution this time, sorry :(
part1 = diff_dist[0] * diff_dist[2]
part2 = arrangements_cnt
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))