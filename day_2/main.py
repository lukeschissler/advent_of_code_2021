fn = "input.txt"

with open(fn, 'r') as f:
    commands = f.readlines()

commands = [x.strip().split(' ') for x in commands]
commands = [(x, int(y)) for x, y in commands]

# PART 1

horizontal = 0
depth = 0
for direction, quantity in commands:
    match direction:
        case 'forward':
            horizontal += quantity
        case 'down':
            depth += quantity
        case 'up':
            depth -= quantity

print(horizontal * depth)

# PART 2

horizontal = 0
depth = 0
aim = 0
for direction, quantity in commands:
    match direction:
        case 'forward':
            horizontal += quantity
            depth += aim * quantity
        case 'down':
            aim += quantity
        case 'up':
            aim -= quantity

print(horizontal * depth)