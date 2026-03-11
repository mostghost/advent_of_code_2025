import imports as imp


def pad_map(map):
    line_width = len(map[0]) + 2
    new_map = []

    for line in map:
        line = "." + line + "."
        new_map.append(line)

    new_map.insert(0, "." * line_width)
    new_map.append("." * line_width)

    return new_map


def check_rolls(map, x, y):

    cat_a = map[y - 1][x - 1 : x + 2]
    cat_b = map[y][x - 1]
    cat_c = map[y][x + 1]
    cat_d = map[y + 1][x - 1 : x + 2]
    cat = cat_a + cat_b + cat_c + cat_d

    if cat.count('@') < 4:
        return True
    else:
        return False


map = imp.dayfour(False)

map = pad_map(map)

height = len(map)
width = len(map[0])

count = 0

for i_height, line in enumerate(map):
    if i_height == 0 or i_height == height - 1:
        continue

    for i_width, char in enumerate(line):
        if i_width == 0 or i_width == width - 1:
            continue

        if char == '@':
            if check_rolls(map, i_width, i_height):
                count += 1

print(count)