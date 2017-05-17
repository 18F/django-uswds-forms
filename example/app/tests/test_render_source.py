from django.test import TestCase
from ..render_source import clean_python_source, clean_template_source


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
