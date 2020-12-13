input = open("Day12/input.txt").read()
instructions = input.splitlines()

north = 0
east = 90
south = 180
west = 270

# Part 1
pos = [0, 0] # [WE, NS]
facing = east

for instruction in instructions:
    inst = instruction[:1]
    val = int(instruction[1:])
    if inst in 'RL':
        if inst == 'L': val = 360 - val
        facing = (facing + val) % 360
        continue
    idx, f = 0, 0
    if inst in 'F':
        if facing == north: inst = 'N'
        if facing == east: inst = 'E'
        if facing == south: inst = 'S'
        if facing == west: inst = 'W'
    if inst in 'WE': idx = 0
    if inst in 'NS': idx = 1
    if inst in 'NE': f = 1
    if inst in 'SW': f = -1
    pos[idx] += f * val

print(sum([abs(p) for p in pos]))

# Part 2
ship = [0, 0]
wayp = [10, 1]

for instruction in instructions:
    inst = instruction[:1]
    val = int(instruction[1:])
    if inst in 'RL':
        if inst == 'L': val = 360 - val
        dist = [wayp[i]-ship[i] for i in [0,1]]
        while (val > 0):
            dist = [dist[1], -dist[0]]
            val -= 90
        wayp = [ship[i]+dist[i] for i in [0,1]]
        continue
    idx, f = 0, 0
    if inst in 'F':
        move = [val * (wayp[i]-ship[i]) for i in [0,1]]
        ship = [ship[i] + move[i] for i in [0,1]]
        wayp = [wayp[i] + move[i] for i in [0,1]]
        continue
    if inst in 'WE': idx = 0
    if inst in 'NS': idx = 1
    if inst in 'NE': f = 1
    if inst in 'SW': f = -1
    wayp[idx] += f * val

print(sum([abs(p) for p in ship]))