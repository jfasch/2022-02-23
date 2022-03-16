import sys
import userdb_csv

users = userdb_csv.read_header(sys.argv[1])
for user in users:
    print(f'ID:{user.id}, Firstname:{user.firstname}, Lastname:{user.lastname}, Date of birth: {user.birth}')
