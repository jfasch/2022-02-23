import userdb_csv
import userdb_sqlite3

import sys


csvfile = sys.argv[1]
dbfile = sys.argv[2]

db = userdb_sqlite3.UserDB_SQLite3(dbfile)

for u in userdb_csv.read_header(csvfile):
    db.insert(u)
