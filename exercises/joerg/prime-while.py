import sys

number = int(sys.argv[1])

if number == 1:
    print('not prime')
    sys.exit()

divisor_candidate = 2
while divisor_candidate < number/2:
    if number % divisor_candidate == 0:
        print('not prime')
        divisor_found = True
        break
    else:
        divisor_candidate += 1
else:
    print('prime')
