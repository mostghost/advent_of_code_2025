instructions = []

with open("dayone/input.txt", "r") as fh:
    for line in fh:
        instructions.append((line[0], line[1:].strip()))

dial = 50
zero_count = 0

for cycle in instructions:
    direction = cycle[0]
    amount = int(cycle[1])

    # Grab the number of full turns and clip just the remainder
    turns = int(amount / 100)
    rem = amount % 100

    zero_count += turns

    match direction:
        case "L":
            for _ in range(rem):
                dial -= 1
                dial = dial % 100
                if dial == 0:
                    zero_count += 1

        case "R":
            for _ in range(rem):
                dial += 1
                dial = dial % 100
                if dial == 0:
                    zero_count += 1

print(zero_count)
