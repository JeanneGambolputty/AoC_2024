import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day10.txt')
r = open(my_local_file,  "r")

source = r.read()
lines = source.strip().split('\n')

# find trailheads, check orthogonal neigbours, repeat if height increments by 1, find paths that reach 9
trailheads = [(row, col) for row, line in enumerate(lines) for col, l in enumerate(line) if l == '0']
directions = [(-1, 0), (0, 1), (1,0), (0, -1)] # 0: up, 1: right, 2: down, 3: left
total_score = 0

from collections import deque

# at each increment update list of coordinates and height, check if former & latter match and
## Part 1: unique positions of 9
## Part 2: unique paths that reach 9
for start_row, start_col in trailheads:

    """ Part 1:
    queue =  deque([(start_row, start_col, 0)])  #current_height initialised at 0 at trailhead
    visited = set()
    nines_reached = set() """
    # list of tuples of coordinates and height PLUS path (Part 2)
    queue = deque([(start_row, start_col, 0, [(start_row, start_col)])])
    paths_to_nine = set()
    
    while queue:
        #row, col, current_height = queue.popleft() #Part 1
        row, col, current_height, path = queue.popleft()

        # skip processing of visited positions (Part 1)
        #if (row, col) in visited:
            #continue
        #visited.add((row, col))
        
        # when 9 is reached, add unique position
        if lines[row][col] == '9':
            #nines_reached.add((row, col)) #Part 1
            paths_to_nine.add(tuple(path))
            continue
        
        # iterate through 4 directions, if within grid & single increment repeat iteration, and update list
        next_height = current_height + 1
        for r, c in directions:
            new_row, new_col = row + r, col + c
            
            if 0 <= new_row < len(lines) and 0 <= new_col < len(lines[0]):
                if lines[new_row][new_col] == str(next_height):
                    #queue.append((new_row, new_col, next_height)) #Part 1
                    new_path = path + [(new_row, new_col)]
                    queue.append((new_row, new_col, next_height, new_path))
    
    #total_score += len(nines_reached) #Part 1: get number of unique 9's reached
    total_score += len(paths_to_nine) #Part 2: get distinct paths to any 9

#print(f"Part 1: {total_score}")
print(f"Part 2: {total_score}")