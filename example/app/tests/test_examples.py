import abc
from unittest import SkipTest
from unittest.mock import patch
from typing import Dict
from django.test import TestCase, override_settings, RequestFactory
from django.shortcuts import render
from django.forms.renderers import Jinja2, DjangoTemplates
from django.conf import settings

from ..views import EXAMPLES


class SmokeTests(TestCase):
    def test_all_examples_return_200(self):
        for ex in EXAMPLES.values():
            res = self.client.get('/example/' + ex.basename)
            self.assertEqual(res.status_code, 200)


@override_settings(
    TEMPLATES=[settings.DJANGO_TEMPLATE_BACKEND,
               settings.JINJA2_TEMPLATE_BACKEND]
)
class TemplateEngineParityTests(TestCase):
    def make_renderer(self, engine_name, form_renderer):
        def force_render_using_engine(req, template_name, ctx):
            ctx['form'].renderer = form_renderer
            return render(req, template_name, ctx, using=engine_name)
        return force_render_using_engine

    def render_example(self, request, example, renderer):
        with patch.object(example.module, 'render', renderer):
            content = example.render(request)
        return '\n'.join([
            line for line in content.split('\n')
            if 'csrfmiddlewaretoken' not in line
        ])

    def test_all_examples_render_the_same_with_different_engines(self):
        self.maxDiff = 5000
        factory = RequestFactory()
        for ex in EXAMPLES.values():
            django = self.render_example(
                factory.get('/'),
                ex,
                self.make_renderer('django', DjangoTemplates())
            )

            jinja2 = self.render_example(
                factory.get('/'),
                ex,
                self.make_renderer('jinja2', Jinja2())
            )

            self.assertHTMLEqual(
                django,
                jinja2,
                'renders of "{}" example must match'.format(ex.basename)
            )


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