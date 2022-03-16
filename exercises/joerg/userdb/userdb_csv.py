import csv

class User:
    pass

def read_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    userlist = []
    for id, firstname, lastname, birth in rdr:
        user = User()
        user.id = int(id)
        user.firstname = firstname
        user.lastname = lastname
        user.birth = birth

        userlist.append(user)
    
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

        user = User()
        user.id = int(id)
        user.firstname = firstname
        user.lastname = lastname
        user.birth = birth

        userlist.append(user)

    return userlist
