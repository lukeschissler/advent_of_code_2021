fn = "input.txt"

with open(fn, 'r') as f:
    measurements = f.readlines()

measurements = [int(x.strip()) for x in measurements]

# PART 1

count = 0
for i in range(len(measurements)-1):
    if int(measurements[i+1]) > int(measurements[i]):
        count += 1

for i in range(10):
    print(i)

print(count)

# PART 2

count2 = 0
for i in range(len(measurements)-3):
    window_one = sum(measurements[i:i+3])
    window_two = sum(measurements[i+1:i+4])
    if window_two > window_one:
        count += 1

print(count2)