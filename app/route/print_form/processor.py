from app.route.print_form.provider import Provider
from app.api.base import base_name as names
from app.api.base.base_sql import Sql


def get_print_form(args):
    """
    Метод для получения данных о печатной
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_print_form(args)

    # TODO КОСТЫЛЬ
    if isinstance(answer, list) and len(answer) == 1:
        answer = answer[0]
    if answer is None:
        _dict = {}
        for f in names.print_form_fields:
            _dict[f] = ''
    return answer or _dict


def update_print_form(args):
    """
    Метод для добавлени/обновления записи пф
    :param args:
    :return:
    """
    provider = Provider()
    query = """
              select 1 from "Организация" where id_user = '{id_user}'
               """
    exists = Sql.exec(query=query, args=args)
    if exists:
        answer = provider.update_print_form(args)
    else:
        answer = provider.insert_print_form(args)
    return answer
