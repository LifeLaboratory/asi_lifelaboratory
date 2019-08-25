# coding=utf-8
from app.api.base import base_name as names
from app.route.profile.processor import *
from app.api.base.base_router import BaseRouter


class Profile(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.LOGIN, names.PASSWORD, names.NAME,
                     names.DESCRIPTION, names.TITLE, names.PHOTO, names.CARD]

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_profile(args)
        return answer or {}

    def post(self):
        self._read_args()
        answer = update_profile(self.data)
        return answer or {}
