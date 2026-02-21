import imports as imp

banks = imp.daythree()

total_charge = 0


# Brute force crawl down from the top possible result - this will check every
# bank to see if '99' is possible, then '98', etc.
# There are only 200 banks to choose from, and most should probably have something
# at the top half of the spectrum, limiting results.

brute_possibles = range(99, 10, -1)


def crawl_bank(bank, first, second, candidate):
    for i, str_num in enumerate(bank):
        num = int(str_num)

        if num == first:
            second_half = bank[i + 1 :]

            for str_num in second_half:
                num = int(str_num)

                if num == second:
                    return candidate


for bank in banks:
    for brute in brute_possibles:
        first, second = str(brute)
        first = int(first)
        second = int(second)

        potential = crawl_bank(bank, first, second, brute)
        if potential:
            print(f"Bank was {bank}, brute was {brute}, candidate is {potential}")
            total_charge += potential
            break

print(total_charge)