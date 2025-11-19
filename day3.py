import os
my_local_file = os.path.join(os.path.dirname(__file__), 'day3.txt')
r = open(my_local_file,  "r")

source = r.read()
import re

## Part 1: return sum of multiplication of valid numbers

# regex for pattern search to find valid number pairs
pattern = r'mul\((\d{1,3}),(\d{1,3})\)' # Pattern WITH parentheses (creates capture groups)
valid_pairs = re.findall(pattern, source)
print(f"Part 1: {sum(int(match1) * int(match2) for match1, match2 in valid_pairs)}")


## Part 2: return sum of multiplication of valid numbers if preceded by valid instructions

# get valid numbers and position of first character
matches = re.finditer(pattern, source)
matches_list = []
for match in matches:
    #print(match.groups(),match.group(1),match.group(2))
    matches_list.append([match.groups(), match.start()])

# get valid instructions and position of first character
instruction = r"do\(\)|don't\(\)"
instructions = re.finditer(instruction, source)
instructions_list = []
for inst in instructions:
    instructions_list.append([inst.group(), inst.start()])
    #print(inst.group(), inst.end())

preceding_instruction = "do()"
result = 0

for m in matches_list:
    for i in instructions_list:
        if i[1] < m[1]:
            preceding_instruction = i[0]
        else:
            break

    if preceding_instruction == "don't()":
        pass
        #print('pass', m[1])
    else:
        x, y = m[0]
        result += int(x) * int(y)
        #print('run', m[1])

print(f"Part 2: {result}")