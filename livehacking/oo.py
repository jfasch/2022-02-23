class UserRecord:
    def __init__(self, firstname, lastname, birth):
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth

joerg = UserRecord(firstname='Joerg', lastname='Faschingbauer',
                   birth='19.06.1966')
caro = UserRecord(firstname='Caro', lastname='Faschingbauer',
                   birth='25.04.1997')

print('JOERG:')
print(joerg.firstname)
print(joerg.lastname)
print(joerg.birth)

print('CARO:')
print(caro.firstname)
print(caro.lastname)
print(caro.birth)
