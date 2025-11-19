import os
from math import gcd
my_local_file = os.path.join(os.path.dirname(__file__), 'day8.txt')
r = open(my_local_file, "r")
source = r.read()
lines = source.strip().split('\n')

# get unique antennae, and their coordinates
# antennae = list(set(l for line in lines for l in line if l != '.'))
coordinates = {}
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char != '.':
            coordinates.setdefault(char, []).append((row, col))

# get distance between all sets of coordinates for each antenna
antinodes = set()
for antenna, positions in coordinates.items():
    if len(positions) >= 2:
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                pos1 = positions[i]
                pos2 = positions[j]

                row_diff = pos2[0] - pos1[0]
                col_diff = pos2[1] - pos1[1]
                g = gcd(abs(col_diff), abs(row_diff))  #part 2 (use gcd to normalise direction vector)
                step_col = col_diff // g  #part 2 (normalised: smallest step in that direction)
                step_row = row_diff // g #part 2 (stepping through grid points along a line)

                ## Part 1: use calculated difference to place antinodes that are not off grid
                #if 0 <= pos1[0] - row_diff <= len(lines) -1 and 0 <= pos1[1] - col_diff <= len(lines[pos1[0] - row_diff]) -1:
                    #antinode1 = (pos1[0] - row_diff, pos1[1] - col_diff)
                    #antinodes.add(antinode1)
                
                #if 0 <= pos2[0] + row_diff <= len(lines) -1 and 0 <= pos2[1] + col_diff <= len(lines[pos2[0] - row_diff]) -1:
                    #antinode2 = (pos2[0] + row_diff, pos2[1] + col_diff)
                    #antinodes.add(antinode2)

                ## Part 2: place antinodes at every grid point along the line between two antennae
                # from pos1 move backwards till edge of grid
                current = pos1
                while 0 <= current[0] < len(lines) and 0 <= current[1] < len(lines[0]):
                    antinodes.add(current)
                    current = (current[0] - step_row, current[1] - step_col)

                # from pos1 move forwards until pos2
                current = (pos1[0] + step_row, pos1[1] + step_col)
                while 0 <= current[0] <= pos2[0] and 0 <= current[1] <= pos2[1]:
                    antinodes.add(current)
                    current = (current[0] + step_row, current[1] + step_col)

                # from pos2 move backwards till edge of grid
                current = (pos2[0] + step_row, pos2[1] + step_col)
                while 0 <= current[0] < len(lines) and 0 <= current[1] < len(lines[0]):
                    antinodes.add(current)
                    current = (current[0] + step_row, current[1] + step_col)

#print(f"Part 1: {len(antinodes)}")
print(f"Part 2: {len(antinodes)}")