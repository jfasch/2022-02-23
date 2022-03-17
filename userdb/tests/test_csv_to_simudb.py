import userdb_csv
import simu_userdb

def test_ok():
    users = userdb_csv.read_header('tests/Users-header-cp1252.csv')
    db = simu_userdb.SimuUserDB()
    for u in users:
        db.insert(u)

    assert db.search(1) is not None
    assert db.search(2) is not None
    assert db.search(3) is not None
    assert db.search(4) is not None
    assert db.search(5) is not None
