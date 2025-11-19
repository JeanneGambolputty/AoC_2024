import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day5.txt')
r = open(my_local_file, "r")
source = r.read()
lines = source.strip().split('\n')
rules = [] # list of strings
updates = []  # list of lists of integers

for line in lines:
    if '|' in line:
        rules.append(line)
    elif ',' in line:
        updates.append(list(map(int, line.split(','))))

## Part 1: sum of middle values of valid updates
count1 = 0

## Part 2: sum of middle values of corrected invalid updates
count2 = 0

from functools import cmp_to_key

def compare_pages(x, y): # wrapper function to be used with sorted()
    for rule in rules:
        before, after = map(int, rule.split("|"))
        if before == x and after == y:
            return -1  # x is to the LEFT of y  →  [x ... y]
        elif before == y and after == x:
            return 1   # x is to the RIGHT of y →  [y ... x]
    return 0  # no rule found, they're equivalent for sorting


for update in updates:
    is_valid = True
    
    # check each update against rules
    for rule in rules:
        before, after = map(int, rule.split("|"))
        
        # for every rule, check if both numbers are in update and get positions
        if before in update and after in update:
            before_pos = update.index(before) # position of first number
            after_pos = update.index(after) # position of second number
            
            # rule violated if update contains an invalid pair ('before' comes after 'after')
            if before_pos > after_pos:
                is_valid = False
                break
    
    # if update valid, add its middle value (Part 1)
    if is_valid:
        mid_pos = len(update) // 2
        count1 += update[mid_pos]

    # if update invalid, correct order and add its middle value (Part 2)
    if not is_valid:
        update_reordered = sorted(update, key=cmp_to_key(compare_pages))
        mid_pos = len(update_reordered) // 2
        count2 += update_reordered[mid_pos]

print(f"Part 1: {count1}")
print(f"Part 2: {count2}")