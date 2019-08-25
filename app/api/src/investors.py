from app.api.sql.investor_provider import Provider
from app.api.base import base_name as names
import json


def get_investors():
    """
    Метод для получения данных о инвесторах
    :param args:
    :return:
    """
    provider = Provider()
    answer = provider.get_investors()
    return answer
