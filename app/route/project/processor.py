from app.route.project.provider import Provider
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

    # TODO КОСТЫЛЬ
    if isinstance(answer, list) and len(answer) == 1:
        answer = answer[0]
        if answer.get('budget'):
            answer['budget'] = float(answer.get('budget'))
    elif isinstance(answer, list):
        for a in answer:
            a['budget'] = float(a.get('budget'))
    return answer


def get_project_category(args):
    """
    Метод для получения данных о категориях проекта
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_project_category(args)
    return answer


def get_project_budget(args):
    """
    Получение бюджета проекта
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_budget(args)
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
