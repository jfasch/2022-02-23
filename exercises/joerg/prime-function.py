import sys


class DefinitionsMengeViolated(Exception):
    def __init__(self, the_number):
        super().__init__(f'primeness not defined for {the_number}')

def is_prime(num):
    if num < 1:
        raise DefinitionsMengeViolated(num)

    if number == 1:
        return False
    
    for divisor_candidate in range(2, num//2 + 1):
        if num % divisor_candidate == 0:
            return False
    else:
        return True


try:
    if is_prime(int(sys.argv[1])):
        print('prime')
    else:
        print('not prime')
except DefinitionsMengeViolated as e:
    print('Benutzer, du solltest AHS Mathematik nachholen:', e)
    sys.exit(1)
