# coding=utf-8
from app.api.base import base_name as names
from app.route.document.processor import get_documents
from app.api.base.base_router import BaseRouter


class Documents(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_DOCUMENT, names.ID_PROJECT, names.ID_USER]

    def post(self):
        self._read_args()
        answer = get_documents(self.data)
        return answer or {}
