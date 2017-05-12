from django.test import TestCase

from .views import EXAMPLES


class AppTests(TestCase):
    def test_home_returns_200(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_nonexistent_example_returns_404(self):
        res = self.client.get('/example/zzz')
        self.assertContains(res, 'Example not found', status_code=404)

    def test_all_examples_return_200(self):
        for ex in EXAMPLES.values():
            res = self.client.get('/example/' + ex.basename)
            self.assertEqual(res.status_code, 200)


class EverythingExampleTests(TestCase):
    url = '/example/everything'

    def test_empty_post_shows_errors(self):
        res = self.client.post(self.url, {})
        self.assertContains(res, 'Submission unsuccessful')

    def test_non_field_errors_are_displayed(self):
        res = self.client.post(self.url, {
            'trigger_non_field_error': 'on',
        })
        self.assertContains(res, 'This is the non-field error you requested')

    def test_valid_post_shows_success(self):
        res = self.client.post(self.url, {
            'president': 'washington',
            'park': 'foo',
            'date_1': '4',
            'date_2': '28',
            'date_0': '2016',
        })
        self.assertContains(res, 'Submission successful')
