input_location = './input/day2.txt'

reports = []
with open(input_location) as f:
    for line in f.readlines():
       reports.append([int(num) for num in line.strip().split()])

# Part 1
num_safe = 0
for report in reports:
    if (sorted(report)==report or sorted(report, reverse=True)==report) and len(report) == len(set(report)):
        steps = [abs(report[i] - report[i - 1]) for i in range(1, len(report))]
        if min(steps) >= 1 and  max(steps) <=3:
            num_safe += 1

# Part 2
# fuck this one already 

