import sys
import csv


filename = sys.argv[1]

f = open(filename, encoding='cp1252')
rdr = csv.reader(f, delimiter=';', quotechar='"')

for id, firstname, lastname, birth in rdr:
    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')
