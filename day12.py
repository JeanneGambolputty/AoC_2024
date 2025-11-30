import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day12.txt')
r = open(my_local_file,  "r")
source = r.read()

plots = source.strip().split('\n')
visited = set()
total_price = 0

# group plots denoted by the same character by checking orthogonal neighbours
def set_region(grid, row_centre, col_centre, char):
    visited.add((row_centre, col_centre)) #no redundant checks of neighbours already checked or that were centres
    queue = [(row_centre, col_centre)] #list to add plots / their neighbours to check
    region = [(row_centre, col_centre)] #list to add plots of the same character within bounds
    
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == char):
                visited.add((nr, nc))
                region.append((nr, nc))
                queue.append((nr, nc))
    
    return region

# Part 1: region perimeter defined by total count of edges
def draw_perimeter(grid, region, char):
    perimeter = 0
    for r, c in region:
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            # edge found if out of bounds or different character
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] != char:
                perimeter += 1
    return perimeter

# Part 2: region perimeter defined by total count of corners
def count_corners(grid, region):
    region_set = set(region) #faster lookups
    corners = 0
    for r, c in region:
        
        # top-left corner
        up = (r-1, c) in region_set
        left = (r, c-1) in region_set
        up_left = (r-1, c-1) in region_set
        if not up and not left:
            corners += 1
        elif up and left and not up_left:
            corners += 1
        
        # top-right corner
        right = (r, c+1) in region_set
        up_right = (r-1, c+1) in region_set
        if not up and not right:
            corners += 1
        elif up and right and not up_right:
            corners += 1
        
        # bottom-left corner
        down = (r+1, c) in region_set
        left = (r, c-1) in region_set
        bottom_left = (r+1, c-1) in region_set
        if not down and not left:
            corners += 1
        elif down and left and not bottom_left:
            corners += 1
        
        # bottom-right corner
        right = (r, c+1) in region_set
        bottom_right = (r+1, c+1) in region_set
        
        if not down and not right:
            corners += 1
        elif down and right and not bottom_right:
            corners += 1
    
    return corners

# get price by mutiplying number of combined plots (list of plot coordinates) by
## Part 1 - perimeter: count each exposed edge segment
## Part 2 - corners: count continuous straight sides (not individual segments)
for row in range(len(plots)):
    for col in range(len(plots[0])):
        if (row, col) not in visited:
            char = plots[row][col]
            region = set_region(plots, row, col, char) #floods outwards to find entire connected region via BFS
            area = len(region)
            #perimeter = draw_perimeter(plots, region, char) #part 1
            #total_price += area * perimeter                 #part 1
            sides = count_corners(plots, region)
            total_price += area * sides

#print(f"Part 1: {total_price}")
print(f"Part 2: {total_price}")