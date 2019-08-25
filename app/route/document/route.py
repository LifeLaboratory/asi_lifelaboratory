# coding=utf-8
from app.route.document.processor import *
from app.api.base.base_router import BaseRouter


class Document(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_DOCUMENT, names.URL, names.TITLE, names.TYPE]

    def post(self):
        self._read_args()
        answer = update_document(self.data)
        return answer or {}


class GetDocument(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = [names.ID_DOCUMENT, names.URL, names.TITLE, names.TYPE]

    def get(self, id_document):
        args = {
            names.ID_DOCUMENT: id_document
        }
        answer = get_document(args)
        return answer or {}