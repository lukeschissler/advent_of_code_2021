import re
fn = "input.txt"

with open(fn, 'r') as f:
    vents = f.readlines()

vents = [re.split('-> |,', x) for x in vents]
vents = [[int(x.strip()) for x in y] for y in vents]

vent_chart = [[0 for x in range(1000)] for y in range(1000)]

for vent in vents:
    x1, y1, x2, y2 = vent
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            vent_chart[y][x1] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            vent_chart[y1][x] += 1
    else:
        for z in range(max(x1, x2) - min(x1, x2) + 1):
            vent_chart[y1][x1] += 1
            if x2 > x1:
                x1 += 1
            else:
                x1 -= 1
            if y2 > y1:
                y1 += 1
            else:
                y1 -= 1

count = 0
for row in vent_chart:
    for entry in row:
        if entry > 1:
            count += 1

print(count)
