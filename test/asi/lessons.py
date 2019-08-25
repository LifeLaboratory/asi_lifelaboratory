import unittest
import requests as req
from app.config.config import HOST
from app.api.base.base_name import *
from asi.utils import gentext

class TestAuth(unittest.TestCase):
    def test_lesson_create(self):
        s = req.Session()
        genned_text = gentext(6)
        data = {
            URL: genned_text,
            TYPE: 1,
            ID_PROJECT: 1,
            TITLE: genned_text
        }
        r = s.post(HOST + '/lesson', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_lessons_get(self):
        s = req.Session()
        r = s.get(HOST + '/lessons')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_lesson_update(self):
        s = req.Session()
        genned_text = gentext(6)
        data = {
            URL: genned_text,
            TYPE: 1,
            TITLE: genned_text
        }
        r = s.put(HOST + '/lesson/1', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_lesson_delete(self):
        s = req.Session()
        r = s.delete(HOST + '/lesson/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)



if __name__ == '__main__':
    unittest.main()
