import sys

filename = sys.argv[1]
f = open(filename)

for line in f:
    criterion_line = line
    hash_pos = criterion_line.find('#')
    if hash_pos != -1:
        criterion_line = criterion_line[:hash_pos]
    
    criterion_line = criterion_line.strip()
    if len(criterion_line) == 0:
        continue

    print(line, end='')
