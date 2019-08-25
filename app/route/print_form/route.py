# coding=utf-8
from app.route.print_form.processor import *
from app.api.base.base_router import BaseRouter


class PrintForm(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = names.print_form_fields
        self.args.append(names.ID_USER)

    def post(self):
        self._read_args()
        answer = update_print_form(self.data)
        return answer or {}


class GetPrintForm(PrintForm):

    def get(self, id_user):
        args = {
            names.ID_USER: id_user
        }
        answer = get_print_form(args)
        return answer or {}
