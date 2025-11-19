import os
from itertools import product
my_local_file = os.path.join(os.path.dirname(__file__), 'day7.txt')
r = open(my_local_file, "r")
source = r.read()
lines = source.strip().split('\n')

## Parts 1 & 2: sum of test values that checked out against equations

tests = [] # list of integers
equations = []  # list of lists of integers

for line in lines:
    parts = line.split(':')
    tests.append(int(parts[0]))
    equations.append(list(map(int, parts[1].split())))

total_result = 0
# equations: generate all combinations of operators for positions between numbers
for j in range(len(equations)):
    num_operators = len(equations[j]) - 1
    #for ops in product(['+', '*'], repeat=num_operators): #part 1
    for ops in product(['+', '*', '||'], repeat=num_operators):
        result = equations[j][0] 
        for i, op in enumerate(ops):
            if op == '+':
                result = result + equations[j][i+1]
            elif op == '*':
                result = result * equations[j][i+1]
            else: #part 2
                result = int(str(result) + str(equations[j][i+1])) #part 2
        # check equation results against test value
        if result == tests[j]:
            total_result += result
            break

print(f"Part 2: {total_result}")