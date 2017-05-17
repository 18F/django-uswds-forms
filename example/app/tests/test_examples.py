import abc
from unittest import SkipTest
from typing import Dict
from django.test import TestCase

from .util import TestEachExample


class ExamplesReturn200Tests(TestCase, metaclass=TestEachExample):
    def test(self, example):
        res = self.client.get('/example/' + example.basename)
        self.assertEqual(res.status_code, 200)


class ExampleMixin(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def url(self) -> str:
        '''
        URL for example. Must be defined by subclasses.
        '''

    @property
    @abc.abstractmethod
    def valid_post(self) -> Dict[str, str]:
        '''
        Valid POST data for example to succeed. Must be defined by subclasses.
        If the form has no required fields, set this to {}.
        '''

    def test_empty_post_shows_errors(self):
        if self.valid_post == {}:
            raise SkipTest('Form has no required fields')
        res = self.client.post(self.url, {})
        self.assertContains(res, 'Submission unsuccessful')

    def test_valid_post_shows_success(self):
        res = self.client.post(self.url, self.valid_post)
        self.assertContains(res, 'Submission successful')


class RadiosExampleTests(ExampleMixin, TestCase):
    url = '/example/radios'

    valid_post = {
        'president': 'washington',
    }


class CheckboxesExampleTests(ExampleMixin, TestCase):
    url = '/example/checkboxes'

    valid_post = {}  # type: Dict[str, str]


class DateExampleTests(ExampleMixin, TestCase):
    url = '/example/date'

    valid_post = {
        'date_1': '4',
        'date_2': '28',
        'date_0': '2016',
    }


class EverythingExampleTests(ExampleMixin, TestCase):
    url = '/example/everything'

    valid_post = {
        'president': 'washington',
        'park': 'foo',
        'date_1': '4',
        'date_2': '28',
        'date_0': '2016',
    }

    def test_non_field_errors_are_displayed(self):
        res = self.client.post(self.url, {
            'trigger_non_field_error': 'on',
        })
        self.assertContains(res, 'This is the non-field error you requested')
