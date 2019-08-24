from app.api.sql.project_provider import Provider
from app.api.base import base_name as names
import json


def get_project(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_project(args)
    return answer

def update_rec(answer):
    for i in range(len(answer)):
        for j in range(len(answer[i].get('category'))):
            answer[i].get('category')[j] = json.loads(answer[i].get('category')[j])


def get_filter_project(args):
    """
    Метод для получения списка проектов
    :param args:
    :return:
    """
    provider = Provider()
    id_user = args.get(names.ID_USER)
    id_category = args.get(names.ID_CATEGORY)
    args = {
        names.ID_USER: 'and upd."id_user" = %s' % id_user if id_user else 'and true',
        names.ID_CATEGORY: 'and pc."id_category" = any(%s)' % str(id_category) if id_category else 'and true',
    }
    answer = provider.get_filter_project(args)
    update_rec(answer)
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
