import imports as imp

banks = imp.daythree()

total_charge = 0

# As usual part 2 is complicated to make it so that a brute force solution is
# difficult to impossible, so a new solution will be needed.


def candidate_finder(iter, bank):
    """
    This cuts each string down into the searchable portion, then just searches
    for the presence of each number in order, 9-1 . If the number exists in the str
    at all, then the first match will make for the largest possible joltage.
    Then returns that number.

    Returns:
    str_num: String version of the largest number
    short_bank: The remainder of the bank, beyond the first instance of the largest num
    """

    end_index = 12 - iter

    if end_index != 0:
        bank_short = bank[: -(12 - iter)]
    else:
        bank_short = bank

    for i in range(9, 0, -1):
        str_num = str(i)

        if str_num in bank_short:
            found_index = bank.index(str_num)
            # If there are multiple num, index always returns the first.

            return str_num, bank[found_index + 1 :]


for bank in banks:
    joltage = ""
    for i in range(1, 13):
        biggest, bank = candidate_finder(i, bank)

        joltage += biggest

    joltage = int(joltage)

    total_charge += joltage

print(total_charge)
