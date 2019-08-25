# coding=utf-8
from app.route.lesson.processor import *
from app.api.base.base_router import BaseRouter


class Lesson(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self):
        answer = get_lessons()
        return answer or {}


class GetLesson(BaseRouter):

    def __init__(self):
        super().__init__()
        self.args = []

    def get(self, id_lesson):
        args = {
            names.ID_DOCUMENT: id_lesson
        }
        try:
            answer = get_lesson(args)[0]
        except:
            answer = {}
        return answer or {}
