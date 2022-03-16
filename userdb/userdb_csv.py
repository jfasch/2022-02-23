import csv
import user

def read_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    userlist = []
    for id, firstname, lastname, birth in rdr:
        userlist.append(user.User(id, firstname, lastname, birth))
    
    return userlist

def read_header(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.DictReader(f, delimiter=';', quotechar='"')

    userlist = []
    for rec in rdr:
        id = rec['ID']
        firstname = rec['First name']
        lastname = rec['Last name']
        birth = rec['Date of Birth']

        userlist.append(user.User(id, firstname, lastname, birth))

    return userlist
