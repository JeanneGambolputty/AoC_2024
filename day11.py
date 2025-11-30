import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day11.txt')
r = open(my_local_file,  "r")

source = r.read()
stones = source.strip().split()

from collections import defaultdict
stones_dict = defaultdict(int)
# original set of stones to which 3 transformation rules will be applied
# added to a dictionary to count the number of stones
for stone in stones:
    stones_dict[stone] += 1

# get resulting number of stones after
for i in range(75): #number of times transformation rules applied
    new_dict = defaultdict(int)
    for key, val in stones_dict.items():
        if key == '0':
            new_dict['1'] += val
        elif len(key) % 2 == 0:
            mid = len(key) // 2
            left = str(int(key[:mid])) #int to remove leading zeroes
            right = str(int(key[mid:]))
            new_dict[left] += val
            new_dict[right] += val
        else:
            new_dict[str(int(key) * 2024)] += val #int for multiplication
    
    stones_dict = new_dict

print(sum(stones_dict.values()))