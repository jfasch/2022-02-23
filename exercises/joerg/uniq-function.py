def uniq_pure(l):
    retlist = []
    have = set()
    for elem in l:
        if elem not in have:
            have.add(elem)
            retlist.append(elem)
    return retlist

def uniq_fromkeys(l):
    '''using a dictionary because that preserves insertion order, 
    as opposed to a set'''
    return list(dict.fromkeys(l))

input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]

output_list_pure = uniq_pure(input_list)
output_list_fromkeys = uniq_fromkeys(input_list)

print('PURE')
for element in output_list_pure:
    print(' '*4, element)
print('FROMKEYS')
for element in output_list_fromkeys:
    print(' '*4, element)
