
fake_users_db = {
    1: {"id": 1, "name": "Alice"},
    2: {"id": 2, "name": "Bob"},
}

def get_all_users():
    return list(fake_users_db.values())

def get_user_by_id(user_id: int):
    return fake_users_db.get(user_id)
