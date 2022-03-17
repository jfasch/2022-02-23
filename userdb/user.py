class BadUserID(Exception):
    pass

class User:
    def __init__(self, id, firstname, lastname, birth):
        if type(id) != int:
            raise BadUserID('nix id gut ' + str(id))
        
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth = birth
