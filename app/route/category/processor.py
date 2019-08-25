from app.route.category.provider import Provider


def get_user_category(args):
    """
    Метод для получения данных о категориях пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_user_category(args)
    return answer


def get_category(args):
    """
    Метод для получения данных о конкретной категории
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_category(args)
    return answer
