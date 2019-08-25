from app.route.cv.provider import Provider
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
    if args.get(names.ID_CV):
        answer = provider.update_cv(args)
    else:
        try:
            answer = provider.insert_cv(args)[0]
        except:
            answer = {}
    return answer
