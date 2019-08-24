import unittest
import requests as req
from app.config.config import HOST
from app.api.base.base_name import *

class TestAuth(unittest.TestCase):
    def test_get_profile(self):
        s = req.Session()
        r = s.get(HOST + '/profile/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_get_profiles(self):
        s = req.Session()
        r = s.get(HOST+ '/profiles')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_update_profile(self):
        s = req.Session()
        data = {
            NAME: 'Test1',
            DESCRIPTION: 'Test1',
            PHOTO: 'Test1',
            CATEGORIES: [1, 2]
        }
        r = s.put(HOST + '/profile/1', data=data)

if __name__ == '__main__':
    unittest.main()
