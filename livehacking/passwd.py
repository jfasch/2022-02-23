import sys
import csv


filename = sys.argv[1]
f = open(filename, encoding='ascii')
csv_reader = csv.reader(f, delimiter=':')

for user, passwd, uid, gid, description, home, shell in csv_reader:
    print(user, passwd, uid, gid, description, home, shell)
