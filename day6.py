import os
import re
my_local_file = os.path.join(os.path.dirname(__file__), 'day6.txt')
r = open(my_local_file, "r")
source = r.read()
lines = source.strip().split('\n')

for row in range(len(lines)):
    for col, char in enumerate(lines[row]):
        if char == '^':
            start_row = row
            start_col = col
            break

## Part 1: sum of total steps taken
# track movement using directional incremental steps, store visited positions for length measuring
current_row = start_row
current_col = start_col
visited = set()
visited.add((current_row, current_col))
directions = [(-1, 0), (0, 1), (1,0), (0, -1)] # 0: up, 1: right, 2: down, 3: left
direction = 0 # initialising on moving upwards

while True:
    # new coordinates
    row_change, col_change = directions[direction]
    new_row = current_row + row_change
    new_col = current_col + col_change
    if new_row < 0 or new_row >= len(lines) or new_col < 0 or new_col >= len(lines[0]):
        break
    # upon meeting obstacle change direction (without moving forward)
    if lines[new_row][new_col] == '#':
        direction = (direction + 1) % 4
    else: # new coordinates update current position (with new direction - if applicable - updated at last iteration)
        current_row = new_row
        current_col = new_col
        visited.add((current_row, current_col))

print(f"Part 1: {len(visited)}")

## Part 2: count different ways an infinite loop occurs, by placing obstacles (after/not start position)
# place single obstacle to change direction and check against stored visited path
# repeat placement at the next position in the set out path

def check_loop(lines, obstacle_row, obstacle_col):

    current_row = start_row
    current_col = start_col
    directions = [(-1, 0), (0, 1), (1,0), (0, -1)] # 0: up, 1: right, 2: down, 3: left
    direction = 0
    visited = set()
    visited.add((current_row, current_col, direction)) # direction added to confirm loop/same path will be followed

    while True:
        row_change, col_change = directions[direction]
        new_row = current_row + row_change
        new_col = current_col + col_change
        if new_row < 0 or new_row >= len(lines) or new_col < 0 or new_col >= len(lines[0]):
            return False
        if lines[new_row][new_col] == '#' or (new_row == obstacle_row and new_col == obstacle_col):
            direction = (direction + 1) % 4
        else:
            current_row = new_row
            current_col = new_col
            position = (current_row, current_col, direction)
            if position in visited:
                return True
            visited.add(position)

obstacle_positions = 0

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == '.' and not(r == start_row and c == start_col):
            if check_loop(lines, r, c):
                obstacle_positions += 1

print(f"Part 1: {obstacle_positions}")