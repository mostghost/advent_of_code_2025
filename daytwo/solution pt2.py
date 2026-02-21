import imports as imp

ranges = imp.daytwo()
invalids = []

for span in ranges:
    span_list = [*range(span[0], span[1] + 1)]

    for num in span_list:
        str_num = str(num)
        column_num = len(str_num)

        max_size_chunk = (column_num // 2) + 1

        for chunk_size in range(1, max_size_chunk):

            if column_num % chunk_size == 0:
                test_candidate = [
                    str_num[x : x + chunk_size]
                    for x in range(0, column_num, chunk_size)
                ]

                test_set = set(test_candidate)

                if len(test_set) == 1:
                    invalids.append(num)
                    # Once one duplicate is found we can move to the next candidate
                    break

print(sum(invalids))
