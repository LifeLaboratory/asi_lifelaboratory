from app.route.investors.provider import Provider


def get_investors():
    """
    Метод для получения данных о инвесторах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_investors()
    return answer
