input_location = './input/day1-2.txt'

with open(input_location) as f:
    left, right = zip(*[line.strip().split() for line in f.readlines()])

counts = {}
for num in left:
    if num not in counts:
        counts[num] = 0
    counts[num] += right.count(num)

score = 0
for num, count in counts.items():
    score += (int(num) * count)

print(score)
    

