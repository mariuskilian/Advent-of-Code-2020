input = open("Day8/input.txt").read().splitlines()

instructions = [[(l := line.split())[0], int(l[1])] for line in input]
accumulator = 0

# Part 1
def execute(idx):
    global accumulator
    instr = instructions[idx]
    if (instr[0] == "jmp"): return idx + instr[1]
    if (instr[0] == "acc"): accumulator += instr[1]
    return idx + 1

def check_loop():
    global accumulator
    visited = [False] * len(instructions)
    idx = 0
    while 0 <= idx < len(instructions):
        if visited[idx]:
            acc = accumulator
            accumulator = 0
            return 1, acc
        visited[idx] = True
        idx = execute(idx)
    acc = accumulator
    accumulator = 0
    if idx == len(instructions): return 0, acc
    return 2, acc
    
print(check_loop())

# Part 2
def fix_loop():
    for instr in instructions:
        if instr[0] == "nop" and instr[1] > 1:
            instr[0] = "jmp"
            if check_loop()[0] == 0: break
            instr[0] = "nop"
        if instr[0] == "jmp" and -instr[1] >= 0:
            instr[0] = "nop"
            if check_loop()[0] == 0: break
            instr[0] = "jmp"

def copy_instructions(instructions): 
    instructions_copy = instructions.copy()
    for i in range(len(instructions)): instructions_copy[i] = instructions[i].copy()
    return instructions_copy

instructions_og = copy_instructions(instructions)
fix_loop()
print(check_loop())

# Combined solution
instructions = instructions_og
part1 = check_loop()
fix_loop()
part2 = check_loop()
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))