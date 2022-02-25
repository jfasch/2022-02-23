def uniq_generator(l):
    have = set()
    for elem in l:
        if elem not in have:
            have.add(elem)
            yield elem

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]
output_list = uniq_generator(input_list)

for element in output_list:
    print(element)
