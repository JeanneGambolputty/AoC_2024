## Cramer's rule to find button press combinations for claw position to reach each prize

# two equations: X, Y coordinate movements for Button A & Button B
# a * A_X + b * B_X = Prize_X  ... (1)
# a * A_Y + b * B_Y = Prize_Y  ... (2)

# eliminate b to solve for a
# multiply (1) by B_Y and (2) by B_X to make b terms equal in both equations
# a * A_X * B_Y + b * B_X * B_Y = Prize_X * B_Y  ... (1')
# a * A_Y * B_X + b * B_X * B_Y = Prize_Y * B_X  ... (2')
# subtract (2') from (1'), and b terms cancel out:
# (a * A_X * B_Y + b * B_X * B_Y) - (a * A_Y * B_X + b * B_X * B_Y) = Prize_X * B_Y - Prize_Y * B_X
#  a * A_X * B_Y                   - a * A_Y * B_X                  = Prize_X * B_Y - Prize_Y * B_X
# a * (A_X * B_Y - A_Y * B_X)                                       = Prize_X * B_Y - Prize_Y * B_X

# isolate a by dividing both sides by (A_X * B_Y - A_Y * B_X)
# a = (Prize_X * B_Y - Prize_Y * B_X) / (A_X * B_Y - A_Y * B_X)

# denominator (A_X * B_Y - A_Y * B_X) => determinant
# a = (Prize_X * B_Y - Prize_Y * B_X) / det

# similarly, to find b, eliminate a (multiply by A_Y and A_X, then subtract):
# b = (A_X * Prize_Y - A_Y * Prize_X) / det

import os
import re

def extract_digits(filename):
    with open(filename) as f:
        source = f.read()
    blocks = source.strip().split('\n\n')
    
    results = []
    for block in blocks:
        digits = [int(x) for x in re.findall(r'\d+', block)]
        
        a_x, a_y, b_x, b_y, prize_x, prize_y = digits
        results.append({
            'A_X': a_x,
            'A_Y': a_y,
            'B_X': b_x,
            'B_Y': b_y,
            'Prize_X': prize_x + 10000000000000, # part 2: + 10000000000000
            'Prize_Y': prize_y + 10000000000000 # part 2: + 10000000000000
        })
    return results

my_local_file = os.path.join(os.path.dirname(__file__), 'day13.txt')
machines = extract_digits(my_local_file)
costs = 0 #3 tokens to move A_X & A_Y and 1 token to move B_X & B_Y
for machine in machines:
    det = machine['A_X'] * machine['B_Y'] - machine['A_Y'] * machine['B_X']
    if det == 0:
        continue
    a = (machine['Prize_X'] * machine['B_Y'] - machine['Prize_Y'] * machine['B_X']) / det
    b = (machine['Prize_Y'] * machine['A_X'] - machine['Prize_X'] * machine['A_Y']) / det

    if a >= 0 and b >= 0 and a == int(a) and b == int(b):
        a, b = int(a), int(b)
        #if a <= 100 and b <= 100: #part 1: <= 100 presses
        # number of Button A presses and number of Button B presses combined to reach prize * tokens
        cost = a * 3 + b * 1
        costs += cost

print(costs)