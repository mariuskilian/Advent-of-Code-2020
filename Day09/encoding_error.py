input = [int(i) for i in open("Day9/input.txt").read().splitlines()]

# Part 1
def is_idx_valid(idx):
    if not (0 <= idx < len(input)): return False
    if idx < 25: return True
    for j in range(1, 26):
        for k in range(1, j):
            if input[idx] == input[idx-j] + input[idx-k]: return True
    return False

def find_first_outlier():
    for i in range(25, len(input)): 
        if not is_idx_valid(i):
            return input[i]

print(find_first_outlier())

# Part 2
def find_contiguous_list(ref_sum):
    bounds = [0, 1]
    while True:
        if bounds[0] == bounds[1]: return
        if bounds[1] > len(input): return
        if (sb := sum(cont_list := input[bounds[0] : bounds[1]])) == ref_sum: return cont_list
        if sb < ref_sum: bounds[1] += 1
        if sb > ref_sum: bounds[0] += 1

contiguous_list = find_contiguous_list(find_first_outlier())
print(min(contiguous_list) + max(contiguous_list))

# Combined solution
part1 =  find_first_outlier()
contiguous_list = find_contiguous_list(part1)
part2 = min(contiguous_list) + max(contiguous_list)
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))