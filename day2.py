import os

# convert string into int values stored in a list of lists
my_local_file = os.path.join(os.path.dirname(__file__), 'day2.txt')
with open(my_local_file, "r") as f:
    source = f.read()
reports = []
for line in source.strip().split('\n'):
    report = list(map(int, line.split()))
    reports.append(report)

## Part 1: check if each report is valid
#  ie containing all ascending or descending values + acceptble difference size between immediate neighbours
def report_safe(report):
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    all_asc = all([d > 0 for d in diff])
    all_desc = all([d < 0 for d in diff])

    if not(all_asc or all_desc):
        return False
    
    if all([1 <= abs(d) <= 3 for d in diff]):
        return True
    
print(f"Part 1: {sum(1 for report in reports if report_safe(report))}")