class SimuUserDB:
    def __init__(self):
        self.db = {}
    def insert(self, user):
        self.db[user.id] = user
    def search(self, uid):
        found = self.db[uid]
        return found
