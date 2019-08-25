# coding=utf-8
from app.route.budget.processor import *
from app.api.base.base_router import BaseRouter


class Budget(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_USER, names.ID_PROJECT, names.BUDGET]

    def post(self):
        self._read_args()
        answer = update_budget(self.data)
        return answer or {}


class GetBudget(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_budget(args)
        return answer or {}
