input_location = './input/day1.txt'

with open(input_location) as f:
    left, right = zip(*[line.strip().split() for line in f.readlines()])

# Part 1
sum = 0
left = sorted(left)
right = sorted(right)
for i in range(0, len(left)):
    sum += abs(int(left[i])-int(right[i]))
print(sum)

# Part 2
counts = {}
for num in left:
    if num not in counts:
        counts[num] = 0
    counts[num] += right.count(num)

score = 0
for num, count in counts.items():
    score += (int(num) * count)

print(score)