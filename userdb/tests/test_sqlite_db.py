from userdb_sqlite3 import UserDB_SQLite3
from user import User


def test_ok():
    db = UserDB_SQLite3(':memory:')
    db.create_schema()

    u1 = User(1, 'Joerg', 'Faschingbauer', '19.6.1966')
    u2 = User(2, 'Caro', 'Faschingbauer', '25.4.1997')

    db.insert(u1)
    db.insert(u2)

    u1_found = db.search(1)
    assert u1_found.id == u1.id
    assert u1_found.firstname == u1.firstname
    assert u1_found.lastname == u1.lastname
    assert u1_found.birth == u1.birth

    u2_found = db.search(2)
    assert u2_found.id == u2.id
    assert u2_found.firstname == u2.firstname
    assert u2_found.lastname == u2.lastname
    assert u2_found.birth == u2.birth
