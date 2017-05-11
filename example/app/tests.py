from django.test import TestCase


class AppTests(TestCase):
    def test_get_returns_200(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_empty_post_shows_errors(self):
        res = self.client.post('/', {})
        self.assertContains(res, 'Submission unsuccessful')

    def test_non_field_errors_are_displayed(self):
        res = self.client.post('/', {
            'trigger_non_field_error': 'on',
        })
        self.assertContains(res, 'This is the non-field error you requested')

    def test_valid_post_shows_success(self):
        res = self.client.post('/', {
            'president': 'washington',
            'park': 'foo',
            'date_1': '4',
            'date_2': '28',
            'date_0': '2016',
        })
        self.assertContains(res, 'Submission successful')
