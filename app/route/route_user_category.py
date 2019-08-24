# coding=utf-8
from app.api.base import base_name as names
from app.api.src.category import *
from app.api.base.base_router import BaseRouter


class UserCategory(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_user_category(args)
        return answer or {}
