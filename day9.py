import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day9.txt')
r = open(my_local_file, "r")
source = r.read().strip()

# initial disc: convert input into usable format, eg 12345 -> 0..111....22222
disc = []
file_ID = 0
for i, el in enumerate(source): #el is alternatively file_ID (digit) and free space (.)
    nb = int(el)
    if i % 2 == 0:
        disc.extend([str(file_ID)] * nb)
        file_ID += 1
    else:
        disc.extend(['.'] * nb)

## Part 1: replace free space on the left with file_ID on the right, one at a time
left = 0
right = len(disc) -1

while left < right:
    # move pointer rightwards until . index is found
    while left < right and disc[left] != '.':
        left += 1
    # move pointer leftwards until digit index is found
    while left < right and disc[right] == '.':
        right -= 1
    # then swap
    if left < right:
        disc[left], disc[right] = disc[right], disc[left]

checksum = 0
for i, el in enumerate(disc):
    if el == '.':
        break
    else:
        checksum += i * int(el)

print(f"Part 1: {checksum}")

## Part 2: move consecutive blocks with same file_ID - not individual blocks - to the 
##         leftmost free space that can fit them, in decreasing file_ID order

max_file_ID = file_ID -1 #last file_ID had 1 superfluous increment (line 13)

for file_ID in reversed(range(max_file_ID+1)):
    str_file_ID = str(file_ID)
    # get file positions on disc, first position, length of file
    file_positions = [pos for pos, id in enumerate(disc) if id == str_file_ID]
    if not file_positions:
        continue
    file_start = file_positions[0]
    file_size = len(file_positions)
 
    # get first space position on disc, length of space
    current_space_start = None
    space_start = None
    space_size = 0
    for i in range(file_start): #checking positions up to file_start-1
        if disc[i] == '.':
            if space_size == 0:
                current_space_start = i
            space_size += 1
            # set first space position when size meets condition
            if space_size >= file_size:
                space_start = current_space_start
                break
        
        else:
            current_space_start = None
            space_size = 0
    
    # the swap: set values of file_positions to . & values of space positions to digits
    if space_start is not None:
        for file_position in file_positions:
            disc[file_position] = '.'
        for j in range(file_size): #not space_size which could be greater
            disc[space_start + j] = str_file_ID

checksum = 0
for i, el in enumerate(disc):
    if el != '.':
        checksum += i * int(el)

print(f"Part 2: {checksum}")