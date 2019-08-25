# coding=utf-8
from app.api.base import base_name as names
from app.route.category.processor import *
from app.api.base.base_router import BaseRouter


class Category(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_category):
        args = {
            names.ID_CATEGORY: id_category
        }
        answer = get_category(args)
        return answer or {}
