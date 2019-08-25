import unittest
import requests as req
from app.config.config import HOST
from app.api.base.base_name import *
from asi.utils import gentext


class TestAuth(unittest.TestCase):
    def test_register(self):
        s = req.Session()
        genned_data = gentext(6)
        data = {
            LOGIN:  genned_data,
            PASSWORD: genned_data,
            NAME: genned_data
        }

        r = s.post(HOST + '/register', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_auth(self):
        s = req.Session()
        genned_data = gentext(6)
        data = {
            LOGIN: genned_data,
            PASSWORD: genned_data
        }
        r = s.post(HOST + '/auth', data=data)
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

if __name__ == '__main__':
    unittest.main()
