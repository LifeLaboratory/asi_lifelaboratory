from app.route.print_form.provider import Provider
from app.api.base import base_name as names


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
    dates = [names.BIRTHDAY, names.date_passport, names.date_residence, names.exiration_date_residence]
    for d in dates:
        if answer.get(d):
            answer[d] = answer[d].strftime('%d.%m.%Y.')
        else:
            answer[d] = ''
    answer[names.code_another_activity] = ''
    return answer


def update_print_form(args):
    """
    Метод для добавлени/обновления записи пф
    :param args:
    :return:
    """
    provider = Provider()
    if args.get(names.ID_USER):
        answer = provider.update_print_form(args)
    else:
        answer = provider.insert_print_form(args)
    return answer
