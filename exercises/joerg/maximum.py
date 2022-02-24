import sys

number_strings = sys.argv[1:]

numbers = []
for ns in number_strings:
    try:
        numbers.append(int(ns))
    except ValueError:
        print('nix integer:', ns)
        sys.exit(1)

# DEPPERT:
# --------
# !!!!!!!!
# --------

# current_maximum = None
# for number in numbers:
#     print('inspecting', number, ', current maximum:', current_maximum)
#     if current_maximum is None:
#         current_maximum = number
#     elif number > current_maximum:
#             current_maximum = number

# print(current_maximum)


# GSCHEIT:
# --------
# !!!!!!!!
# --------

print(max(numbers))
