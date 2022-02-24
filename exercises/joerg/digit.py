import sys


lookup_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    }

try:
    meine_ziffer_as_int = int(sys.argv[1])
    translation = lookup_table[meine_ziffer_as_int]
    print(translation)
except ValueError:
    print('nix integer:', sys.argv[1])
    sys.exit(1)
except KeyError:
    print('nix ziffer:', sys.argv[1])
    sys.exit(1)
