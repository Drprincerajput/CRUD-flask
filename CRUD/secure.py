from user import User

user = [User(1, 'prince', 'pass'), User(2, 'zoya', 'word')]

username_table = {u.username: u for u in user}
userid_table = {u.id: u for u in user}


def authenticate(username, password):
    user = username_table.get(username, None)
    if user and password == user.password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
