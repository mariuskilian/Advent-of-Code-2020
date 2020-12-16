input = open("Day15/input.txt").read().splitlines()[0].split(',')

from collections import defaultdict

game = defaultdict(int)
for i in range(len(input)-1): game[int(input[i])] = i+1

# Part 1
ref = int(input[-1])
turn = len(input)

def take_turn(game, n=1):
    global ref, turn
    n += turn
    while turn < n:
        next_val = (turn - game[ref]) % turn
        game[ref] = turn
        ref = next_val
        turn += 1
    return game

take_turn(game.copy(), 2020-len(input))
print(ref)

# Part 2
ref = int(input[-1])
turn = len(input)

take_turn(game.copy(), 30000000-len(input))
print(ref)