import pprint
import sys

passwdfile = sys.argv[1]
users = sys.argv[2:]

# -----------------------------------------------------------
# fill userdatabase from passwd file
userdatabase = {}

f = open(passwdfile)

for line in f:
    line = line.rstrip('\n')
    username, password, uid, gid, description, home, shell = line.split(':')
    userdatabase[username] = {
        'uid': int(uid),
        'gid': int(gid),
        'description': description,
        'home': home,
        'shell': shell,
    }

# -----------------------------------------------------------
# search users

for user in users:
    metadata = userdatabase.get(user)
    if metadata is None:
        print(user, 'not found')
    else:
        print(f'''User: {user}
  UID: {metadata["uid"]}
  GID: {metadata["gid"]}
  Home: {metadata["home"]}
  Shell: {metadata["shell"]}
''')
