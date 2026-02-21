def check_testmode(test_mode):
    if test_mode:
        test = "_test"
    else:
        test = ""

    return test


def dayone(test_mode=False):

    test = check_testmode(test_mode)
    instructions = []

    with open(f"dayone/input{test}.txt", "r") as fh:
        for line in fh:
            instructions.append((line[0], line[1:].strip()))

    return instructions


def daytwo(test_mode=False):

    test = check_testmode(test_mode)
    ranges = []

    with open(f"daytwo/input{test}.txt", "r") as fh:
        for line in fh:
            ranges = line.split(",")
            ranges = [x.split("-") for x in ranges]
            ranges = [(int(y[0]), int(y[1])) for y in ranges]

    return ranges


def daythree(test_mode=False):

    test = check_testmode(test_mode)
    banks = []

    with open(f"daythree/input{test}.txt", "r") as fh:
        for line in fh:
            banks.append(line.strip())

    return banks
