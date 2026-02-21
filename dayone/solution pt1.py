import imports as imp

instructions = imp.dayone()
dial = 50
zero_count = 0

for cycle in instructions:
    direction = cycle[0]
    amount = int(cycle[1])

    match direction:
        case "L":
            dial = (dial - amount) % 100
        case "R":
            dial = (dial + amount) % 100

    if dial == 0:
        zero_count += 1

print(zero_count)
