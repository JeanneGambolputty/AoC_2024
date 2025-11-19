import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day4.txt')
r = open(my_local_file,  "r")

source = r.read()
lines = source.strip().split('\n')

## Part 1: count number of pattern occurences
patterns = ['XMAS', 'SAMX']
# horizontal
count = sum(line.count(pattern) for line in lines for pattern in patterns)

# vertical
for i in range(len(lines)):
    vertical = ''
    for line in lines:
        vertical += line[i]
    count += vertical.count('XMAS') + vertical.count('SAMX')

# A B C D
# E F G H
# I J K L
# M N O P

# up-right (\) diagonal, upper right triangle
for y in range(len(lines[0])):
    diagonal = '' # diagonal string starts at lines[0][0], lengthens by moving down in L, next string starts at lines[0][1]
    row, col = 0, y # row increments by 1 (moving down lines), col increments by 1 + y (diagonal moves rightwards)
    while row < len(lines) and col < len(lines[0]): # although each diagonal string's first character is from lines[0]
        diagonal += lines[row][col] # y = 0 & col = 3 diagonal = A F K P; y = 3 & col = 3 diagonal = D
        row += 1
        col += 1 # starts y parsing at one column to the right
    count += diagonal.count('XMAS') + diagonal.count('SAMX')

# down-right (\) diagonal, lower left triangle
for x in range(1, len(lines)): # starts at lines[1][0](skipping row 0 as it's covered above)
    diagonal = '' # moving down in L because subsequent row - inner parsing - has x added to it
    row, col = x, 0 # although each diagonal string's first character (diagonal[0]) is always first of each row (col = 0)
    while row < len(lines) and col < len(lines[0]): # each successive row has fewer rows remaining => shorter diagonals
        diagonal += lines[row][col] # x = 1 & col = 3 diagonal = E J O; x = 3 & col = 3 diagonal = M
        row += 1 # the earlier/smaller the starting row, the more room to travel diagonally before hitting the bottom
        col += 1
    count += diagonal.count('XMAS') + diagonal.count('SAMX')

# up-left (/) diagonal, upper left triangle
for c in range(len(lines[0])-1, -1, -1): # first character is from lines[0]: D, C, B, A
    diagonal = ''
    row, col = 0, c
    while row < len(lines) and col >= 0:
        diagonal += lines[row][col]
        row += 1
        col -= 1
    count += diagonal.count('XMAS') + diagonal.count('SAMX')

# down-left (/) diagonal, lower right triangle
for r in range(1, len(lines)): # starts at lines[1][-1](skipping row 0 as it's covered above)
    diagonal = ''
    row, col = r, len(lines[0])-1 # first character is last of every row
    while row < len(lines) and col >= 0:
        diagonal += lines[row][col]
        row += 1
        col -= 1
    count += diagonal.count('XMAS') + diagonal.count('SAMX')

print(f"Part 1: {count}")

count = 0

def is_valid_pos(row, col):
    return 0 <= row < len(lines) and 0 <= col < len(lines[0])

# check if 'A' is at the centre of an X-MAS
def centre_of_xmas(A_row, A_col):
    
    # get diagonal positions around the centre 'A'
    tl_row, tl_col = A_row - 1, A_col - 1 # top-left diagonal
    br_row, br_col = A_row + 1, A_col + 1 # bottom-right diagonal
    tr_row, tr_col = A_row - 1, A_col + 1 # top-right diagonal  
    bl_row, bl_col = A_row + 1, A_col - 1 # bottom-left diagonal  
    
    # check bounds for neighbour positions
    positions = [(tl_row, tl_col), (br_row, br_col), (tr_row, tr_col), (bl_row, bl_col)]
    if not all(is_valid_pos(r, c) for r, c in positions):
        return False
    
    # get string for both diagonals
    diagonal1 = lines[tl_row][tl_col] + lines[A_row][A_col] + lines[br_row][br_col] # \
    diagonal2 = lines[tr_row][tr_col] + lines[A_row][A_col] + lines[bl_row][bl_col] # /
    
    # check if patterns in both diagonals
    patterns = ['MAS', 'SAM']
    return diagonal1 in patterns and diagonal2 in patterns

# find 'A' positions and check if in X-MAS centres
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] == 'A':
            if centre_of_xmas(row, col):
                count += 1

print(f"Part 2: {count}")