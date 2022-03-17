class DuplicatIDError(Exception):
    pass

class SimuUserDB:
    def __init__(self):
        self.db = {}

    def insert(self, user):
        if user.id in self.db:
            raise DuplicatIDError(str(user.id))
        self.db[user.id] = user

    def search(self, uid):
        found = self.db[uid]
        return found
