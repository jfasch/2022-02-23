from user import User
import sqlite3


class UserDB_SQLite3:
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)

    def create_schema(self):
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE userdb ( uid integer, firstname text, lastname text, birth text );')
        self.connection.commit()

    def insert(self, user):
        cursor = self.connection.cursor()
        cursor.execute(f'insert into userdb values ({user.id}, "{user.firstname}", "{user.lastname}", "{user.birth}");')
        self.connection.commit()

    def search(self, uid):
        cursor = self.connection.cursor()
        resultset = cursor.execute(f'select * from userdb where uid = {uid};')

        users = list(resultset)
        assert len(users) == 1

        uid, firstname, lastname, birth = users[0]
        return User(uid, firstname, lastname, birth)
