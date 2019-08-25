# coding=utf-8
from app.api.base import base_name as names
from app.api.src.ads import *
from app.api.base.base_router import BaseRouter


class Ads(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self):
        answer = get_ads()
        return answer or {}
