# coding=utf-8
from app.api.base import base_name as names
from app.api.src.project import *
from app.api.base.base_router import BaseRouter


class Project(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_DOCUMENT, names.URL, names.TITLE, names.TYPE]

    def post(self):
        self._read_args()
        answer = update_project(self.data)
        return answer or {}


class GetProject(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_DOCUMENT, names.URL, names.TITLE, names.TYPE]

    def get(self, id_project):
        args = {
            names.ID_PROJECT: id_project
        }
        answer = get_project(args)
        return answer or {}
