from app.route.budget.provider import Provider
from app.api.base import base_name as names


def get_budget(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_budget(args)
    return answer


def get_budgets(args):
    """
    Метод для получения данных о документах
    :param args:
    :return:
    """
    provider = Provider()
    id_user = args.get(names.ID_USER)
    args = {
        names.ID_USER: 'and upd."id_user" = %s' % id_user if id_user else 'and true',
    }
    answer = provider.get_budget(args)
    return answer


def get_user_budget(args):
    """
    Метод для получения списка документов пользователя
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_budget(args)
    return answer


def update_budget(args):
    """
    Метод для добавлени/обновления инвестиции
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_USER) and args.get(names.ID_PROJECT):
        answer = provider.insert_budget(args)
    else:
        answer = provider.update_budget(args)
    return answer
