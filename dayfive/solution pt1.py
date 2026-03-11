import imports as imp

ids, ingredients = imp.dayfive(False)

count = 0

for ingred in ingredients:
    for id_range in ids:
        if ingred in range(id_range[0], id_range[1] + 1):
            count += 1
            break

print(count)
