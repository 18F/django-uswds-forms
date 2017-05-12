import abc
from unittest import SkipTest
from typing import Dict
from django.test import TestCase, override_settings

from .views import EXAMPLES
from .example import add_links_to_docs
from .render_source import clean_python_source, clean_template_source


class RenderSourceTests(TestCase):
    def test_clean_python_source_works(self):
        self.assertEqual(
            clean_python_source("'''boop\n'''\nhello()\nthere()\n"),
            "hello()\nthere()"
        )

    def test_clean_template_source_works(self):
        self.assertEqual(
            clean_template_source(r"{% include 'foo' %}" + "\nblah\n"),
            'blah'
        )


@override_settings(DOCS_URL="http://docs/")
class AddLinksToDocsTests(TestCase):
    def test_it_does_nothing_when_docs_have_no_links(self):
        self.assertEqual(add_links_to_docs('foo bar baz'), 'foo bar baz')

    def test_it_hyperlinks_uswds_links(self):
        self.assertEqual(
            add_links_to_docs('foo uswds_forms.UswdsForm baz'),
            'foo <a href="http://docs/reference.html#uswds_forms.UswdsForm">'
            '<code>UswdsForm</code></a> baz'
        )

    def test_it_does_not_hyperlink_final_periods(self):
        self.assertEqual(
            add_links_to_docs('foo uswds_forms.UswdsForm. yup.'),
            'foo <a href="http://docs/reference.html#uswds_forms.UswdsForm">'
            '<code>UswdsForm</code></a>. yup.'
        )


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
