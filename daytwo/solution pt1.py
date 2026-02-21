ranges = []

with open("daytwo/input.txt", "r") as fh:
    for line in fh:
        ranges = line.split(",")
        ranges = [x.split("-") for x in ranges]
        ranges = [(int(y[0]), int(y[1])) for y in ranges]

invalids = []

for span in ranges:
    span_list = [*range(span[0], span[1] + 1)]

    for num in span_list:

        str_num = str(num)

        column_num = len(str_num)

        if column_num % 2 == 0:  # This grabs only nums that could be mirrored
            half = column_num // 2

            L = str_num[:half]
            R = str_num[half:]

            if L == R:
                invalids.append(num)

print(sum(invalids))