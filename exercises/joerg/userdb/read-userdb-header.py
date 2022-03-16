import sys
import csv


filename = sys.argv[1]

f = open(filename, encoding='cp1252')
rdr = csv.DictReader(f, delimiter=';', quotechar='"')

for rec in rdr:
    id = rec['ID']
    firstname = rec['First name']
    lastname = rec['Last name']
    birth = rec['Date of Birth']

    print(f'ID:{id}, Firstname:{firstname}, Lastname:{lastname}, Date of birth: {birth}')
