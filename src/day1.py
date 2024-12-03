input_location = './input/day1.txt'

with open(input_location) as f:
    left, right = zip(*[line.strip().split() for line in f.readlines()])

sum = 0
left = sorted(left)
right = sorted(right)
for i in range(0, len(left)):
    sum += abs(int(left[i])-int(right[i]))
print(sum)
    

