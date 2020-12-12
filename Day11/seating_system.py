input = open("Day11/input2.txt").read()

occupied = '#'
free = 'L'
floor = '.'

# Part 1
seating = [[c for c in row] for row in input.splitlines()]
num_rows = len(seating)
num_cols = len(seating[0])

def change_seat_state_p1(seating, row, col):
    seat = seating[row][col]
    if seat == floor: return False
    occupied_adjacent = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == y == 0: continue
            row_t = row + x
            col_t = col + y
            if 0 <= row_t < num_rows and 0 <= col_t < num_cols:
                if seating[row_t][col_t] == occupied: occupied_adjacent += 1
    if seat == free and occupied_adjacent == 0: return True
    if seat == occupied and occupied_adjacent >= 4: return True
    return False

def simulate_round_p1(seating):
    num_seats_changed = 0
    new_seating = seating.copy()
    for i in range(num_rows):
        new_seating[i] = seating[i].copy()
        for j in range(num_cols):
            if change_seat_state_p1(seating, i, j):
                if seating[i][j] == occupied: new_seating[i][j] = free
                if seating[i][j] == free: new_seating[i][j] = occupied
                num_seats_changed += 1
    return new_seating, num_seats_changed

while True:
    seating, num_seats_changed = simulate_round_p1(seating)
    if num_seats_changed == 0:
        num_occupied = 0
        for row in seating:
            for seat in row:
                if seat == occupied: num_occupied += 1
        print(num_occupied)
        break

# Part 2
seating = [[c for c in row] for row in input.splitlines()]
num_rows = len(seating)
num_cols = len(seating[0])

def change_seat_state_p2(seating, row, col):
    seat = seating[row][col]
    if seat == floor: return False
    occupied_visible = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == y == 0: continue
            f = 1
            while 0 <= (r := row + f*x) < num_rows and 0 <= (c := col + f*y) < num_cols:
                f += 1
                if seating[r][c] == occupied: occupied_visible += 1
                if seating[r][c] != floor: break
    if seat == free and occupied_visible == 0: return True
    if seat == occupied and occupied_visible >= 5: return True
    return False

def simulate_round_p2(seating):
    num_seats_changed = 0
    new_seating = seating.copy()
    for i in range(num_rows):
        new_seating[i] = seating[i].copy()
        for j in range(num_cols):
            if change_seat_state_p2(seating, i, j):
                if seating[i][j] == occupied: new_seating[i][j] = free
                if seating[i][j] == free: new_seating[i][j] = occupied
                num_seats_changed += 1
    return new_seating, num_seats_changed

while True:
    seating, num_seats_changed = simulate_round_p2(seating)
    if num_seats_changed == 0:
        num_occupied = 0
        for row in seating:
            for seat in row:
                if seat == occupied: num_occupied += 1
        print(num_occupied)
        break

# Combined solution
seating = [[c for c in row] for row in input.splitlines()]
num_rows = len(seating)
num_cols = len(seating[0])

def change_seat_state(seating, row, col, occupied_lim, visible):
    seat = seating[row][col]
    if seat == floor: return False
    occupied_seats = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if x == y == 0: continue
            f = 1
            while 0 <= (r := row + f*x) < num_rows and 0 <= (c := col + f*y) < num_cols:
                f += 1
                if seating[r][c] == occupied: occupied_seats += 1
                if not visible: break
                if seating[r][c] != floor: break
    if seat == free and occupied_seats == 0: return True
    if seat == occupied and occupied_seats >= occupied_lim: return True
    return False

def simulate_round(seating, occupied_lim, visible):
    num_seats_changed = 0
    new_seating = seating.copy()
    for i in range(num_rows):
        new_seating[i] = seating[i].copy()
        for j in range(num_cols):
            if change_seat_state(seating, i, j, occupied, visible):
                if seating[i][j] == occupied: new_seating[i][j] = free
                if seating[i][j] == free: new_seating[i][j] = occupied
                num_seats_changed += 1
    return new_seating, num_seats_changed

def count_occupied_seats(seating):
    num_occupied = 0
    for row in seating:
        for seat in row:
            if seat == occupied: num_occupied += 1
    return num_occupied

seating_p1 = seating.copy()
seating_p2 = seating.copy()
for i in range(num_rows):
    seating_p1[i] = seating[i].copy()
    seating_p2[i] = seating[i].copy()
part1 = -1
part2 = -1
while True:
    if part1 < 0:
        seating_p1, num_seats_changed_p1 = simulate_round(seating, 4, False)
        if num_seats_changed_p1 == 0:
            part1 = count_occupied_seats(seating_p1)
    if part2 < 0:
        seating_p2, num_seats_changed_p2 = simulate_round(seating, 5, True)
        if num_seats_changed_p2 == 0:
            part2 = count_occupied_seats(seating_p2)
print("Part 1 solution: " + str(part1))
print("Part 2 solution: " + str(part2))