from app.api.sql.cv_provider import Provider
from app.api.base import base_name as names


def get_user_cv(args):
    """
    Метод для получения данных о категориях пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_user_cv(args)
    return answer


def get_cv():
    """
    Метод для получения всех CV
    :return:
    """
    provider = Provider()
    answer = provider.get_cv()
    return answer


def update_cv(args):
    """
    Метод для добавлени/обновления документа
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_USER):
        answer = provider.update_cv(args)
    else:
        answer = provider.insert_cv(args)
    return answer
