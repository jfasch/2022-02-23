import sys


if len(sys.argv) != 6:
    print('nix da: 6 args will ich')
    sys.exit(1)

print('sys.argv:', sys.argv)
print('sys.argv[0]: ', sys.argv[0])
print('sys.argv[1]: ', sys.argv[1])
print('sys.argv[2]: ', sys.argv[2])
print('sys.argv[3]: ', sys.argv[3])
print('sys.argv[4]: ', sys.argv[4])
print('sys.argv[5]: ', sys.argv[5])


my_number_as_str = sys.argv[5]
print(my_number_as_str, type(my_number_as_str))

my_number_as_int = int(my_number_as_str)
print(my_number_as_int, type(my_number_as_int))
