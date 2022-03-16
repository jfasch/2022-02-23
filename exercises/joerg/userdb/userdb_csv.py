import csv

class User:
    def __init__(self, id, firstname, lastname, birth):
        self.id = int(id)
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

def read_noheader(filename):
    f = open(filename, encoding='cp1252')
    rdr = csv.reader(f, delimiter=';', quotechar='"')

    userlist = []
    for id, firstname, lastname, birth in rdr:
        userlist.append(User(id, firstname, lastname, birth))
    
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

        userlist.append(User(id, firstname, lastname, birth))

    return userlist
