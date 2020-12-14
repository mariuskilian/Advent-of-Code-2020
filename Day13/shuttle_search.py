input = open("Day13/input.txt").read().splitlines()

import math

# Part 1
arrival = int(input[0])
busses = {}
for b in input[1].split(','):
    if b == 'x': continue
    bid = int(b)
    busses[bid] = math.ceil(arrival/bid) * bid
bid = min(busses, key=busses.get)
print(bid * (busses[bid]-arrival))

# Part 2
busses = {}
for i in range(len(b := input[1].split(','))):
    if b[i] == 'x': continue
    busses[int(b[i])] = i

slowest_bus_offset = busses[max(busses)]
for bid in busses: busses[bid] -= slowest_bus_offset

def lcm(a, b): return int(a*b / math.gcd(a,b))

t = 0
t_step = max(busses)
while busses:
    busses_tmp = busses.copy()
    for bid in busses_tmp:
        b_t = t + busses_tmp[bid]
        if b_t < 0 or b_t % bid != 0: continue
        t_step = lcm(t_step, bid)
        del busses[bid]
    if not busses: break
    t += t_step
t -= slowest_bus_offset
print(t)