from unittest.mock import patch
from django.test import TestCase, override_settings, RequestFactory
from django.shortcuts import render
from django.forms.renderers import Jinja2, DjangoTemplates
from django.conf import settings

from .util import TestEachExample


@override_settings(
    TEMPLATES=[settings.DJANGO_TEMPLATE_BACKEND,
               settings.JINJA2_TEMPLATE_BACKEND]
)
class TemplateEngineParityTests(TestCase, metaclass=TestEachExample):
    '''
    This renders each example using its Django and Jinja2 template
    and ensures that both produce the same HTML.
    '''

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

    def test(self, example):
        self.maxDiff = 5000
        factory = RequestFactory()
        django = self.render_example(
            factory.get('/'),
            example,
            self.make_renderer('django', DjangoTemplates())
        )

        jinja2 = self.render_example(
            factory.get('/'),
            example,
            self.make_renderer('jinja2', Jinja2())
        )

        self.assertHTMLEqual(
            django,
            jinja2,
            'renders of "{}" example must match'.format(example.basename)
        )
