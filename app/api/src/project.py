from app.api.sql.project_provider import Provider
from app.api.base import base_name as names


def get_project(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_project(args)
    return answer


def get_filter_project(args):
    """
    Метод для получения списка проектов
    :param args:
    :return:
    """
    provider = Provider()
    args = {
        names.ID_USER: args.get(names.ID_USER),
        names.ID_CATEGORY: args.get(names.ID_CATEGORY),
    }
    answer = provider.get_filter_project(args)
    return answer


def update_project(args):
    """
    Метод для добавлени/обновления документа
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_DOCUMENT):
        answer = provider.update_project(args)
    else:
        answer = provider.insert_project(args)
    return answer
