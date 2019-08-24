from app.api.sql.document_provider import Provider
from app.api.base import base_name as names


def get_document(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_document(args)
    return answer


def get_documents(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    args = {
        names.ID_USER: args.get(names.ID_USER),
        names.ID_DOCUMENT: args.get(names.ID_DOCUMENT),
        names.ID_PROJECT: args.get(names.ID_PROJECT),
    }
    answer = provider.get_documents(args)
    return answer


def get_user_document(args):
    """
    Метод для получения списка документов пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_document(args)
    return answer


def update_document(args):
    """
    Метод для добавлени/обновления документа
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_DOCUMENT):
        answer = provider.update_document(args)
    else:
        answer = provider.insert_document(args)
    return answer
