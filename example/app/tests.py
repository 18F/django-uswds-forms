from django.test import TestCase


class AppTests(TestCase):
    def test_home_loads(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
