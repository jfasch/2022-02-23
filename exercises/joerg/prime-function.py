import sys

def is_prime(num):
    if num < 1:
        raise Exception(f'he oida definitionsmenge!!! ({num})')

    if number == 1:
        return False
    
    for divisor_candidate in range(2, number//2 + 1):
        if number % divisor_candidate == 0:
            return False
    else:
        return True


number = int(sys.argv[1])
try:
    issiejetztprimeoderwas = is_prime(number)
except Exception as e:
    print('Benutzer, du solltest AHS Mathematik nachholen', e)
    sys.exit(1)

if issiejetztprimeoderwas:
    print('prime')
else:
    print('not prime')
