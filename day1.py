import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day1.txt')
with open(my_local_file, "r") as f:
    source = f.read()

left_list = []
right_list = []

# convert string into int values stored in two lists
for line in source.strip().split('\n'):
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

## Part 1: total distance between sorted lists
left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
print(f"Part 1: {total_distance}")

## Part 2: similarity score
from collections import Counter
right_count = Counter(right_list)

similarity_score = sum(right_count[num] * num for num in left_list)
print(f"Part 2: {similarity_score}")
