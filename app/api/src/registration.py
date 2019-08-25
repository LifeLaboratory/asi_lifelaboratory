from app.api.sql.register_provider import Provider


def register(user_data):
    provider = Provider()
    check = provider.check_user(user_data)
    id_user = None
    if not check:
        id_user = provider.register_user(user_data)
        if isinstance(id_user, list):
            id_user = id_user[0]
    else:
        print('Пользователь существует', user_data)
    return id_user
