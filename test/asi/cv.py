import unittest
import requests as req
from app.config.config import HOST

class TestAuth(unittest.TestCase):
    def test_get_ads(self):
        s = req.Session()
        r = s.get(HOST + '/cv/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

    def test_get_ad(self):
        s = req.Session()
        r = s.get(HOST + '/ad/1')
        print(r.text)
        self.assertEqual(r.status_code, 200)
        self.assertIsNotNone(r.text)

if __name__ == '__main__':
    unittest.main()
