# coding=utf-8
from app.route.cv.processor import *
from app.api.base.base_router import BaseRouter


class Cv(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.URL, names.TITLE, names.TYPE, names.DESCRIPTION]

    def get(self):
        answer = get_cv()
        return answer or {}

    def post(self):
        self._read_args()
        print(self.data)
        answer = update_cv(self.data)
        return answer or {}


class GetCv(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_user_cv(args)
        return answer or {}
