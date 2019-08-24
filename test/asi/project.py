import unittest
import requests as req
from app.config.config import HOST
from app.api.base.base_name import *
from asi.utils import gentext

class TestAuth(unittest.TestCase):
    def test_project_create(self):
        s = req.Session()
        genned_text = gentext(6)
        data = {
            TITLE: genned_text,
            DESCRIPTION: genned_text,
            NAME: genned_text,
            ID_USER: 1,
            CATEGORIES: [1, 2],
            BUDGET: 1600.99,
            RATE: 4.2
        }
        r = s.get(HOST + '/category', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_projects_get(self):
        s = req.Session()
        r = s.get(HOST + '/project')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_project_get(self):
        s = req.Session()
        r = s.get(HOST + '/project/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_project_delete(self):
        s = req.Session()
        r = s.delete(HOST + '/project/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_project_update(self):
        s = req.Session()
        genned_text = gentext(6)
        data = {
            TITLE: genned_text,
            DESCRIPTION: genned_text,
            NAME: genned_text,
            PHOTO: genned_text,
            ID_USER: 1,
            CATEGORIES: [1, 2],
            BUDGET: 2303.15,
            RATE: 3.2
        }
        r = s.put(HOST + '/project/1', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_project_filter(self):
        s = req.Session()
        data = {
            ID_USER: 1,
            ID_CATEGORY: 1
        }
        r = s.put(HOST + '/project/1', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

if __name__ == '__main__':
    unittest.main()
