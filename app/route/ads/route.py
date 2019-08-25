# coding=utf-8
from app.route.ads.processor import *
from app.api.base.base_router import BaseRouter


class Ads(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self):
        answer = get_ads()
        return answer or {}
