import re
from pathlib import Path
from typing import Match
from django.conf import settings
from django.utils.safestring import SafeString
from django.utils.module_loading import import_string
from django.urls import reverse

from .render_source import render_template_source, render_python_source

APP_DIR = Path(__file__).resolve().parent
PY_DIR = APP_DIR / 'examples'
TEMPLATES_DIR = APP_DIR / 'templates' / 'examples'
JINJA2_DIR = APP_DIR / 'jinja2' / 'examples'


def add_links_to_docs(text: str) -> str:
    '''
    This somewhat hacky function takes a string of documentation and
    adds Sphinx documentation hyperlinks to anything that looks like a
    reference to a uswds_forms object.

    Note that it's assumed the text passed in is trusted.
    '''

    def hyperlink(match: Match) -> str:
        end_text = ''
        objname = match.group(0)
        if objname.endswith('.'):
            end_text = objname[-1]
            objname = objname[:-1]
        _, short_objname = objname.split('.', 1)

        # Try importing the string, to make sure it's not pointing at
        # a symbol that doesn't actually exist.
        import_string(objname)

        return '<a href="{}reference.html#{}"><code>{}</code></a>{}'.format(
            settings.DOCS_URL,
            objname,
            short_objname,
            end_text
        )

    text = re.sub(
        r'uswds_forms\.([a-zA-Z0-9_.]+)',
        hyperlink,
        text
    )
    return text


class Example:
    def __init__(self, basename: str, load: bool=False) -> None:
        self.basename = basename
        self.template_path = TEMPLATES_DIR / (basename + '.html')
        self.jinja2_path = JINJA2_DIR / (basename + '.html')
        self.python_path = PY_DIR / (basename + '.py')

        if load:
            self.load()

    def load(self):
        self.view = import_string('app.examples.' + self.basename + '.view')
        self.module = import_string('app.examples.' + self.basename)

        docstr = import_string('app.examples.' + self.basename + '.__doc__')
        self.name, description = docstr.split('\n\n', 1)
        self.description = SafeString(add_links_to_docs(description))
        self.python_source = render_python_source(self.python_path)

    @property
    def template_source(self):
        return render_template_source(self.template_path)

    @property
    def jinja2_source(self):
        return render_template_source(self.jinja2_path)

    @property
    def url(self):
        return reverse('example', args=(self.basename,))

    def render(self, request):
        # This is sort of weird because we're decoding the
        # content in a HttpResponse; it's not an ideal API,
        # but we want the examples be as conventional as
        # possible so they don't confuse readers, and having
        # them return HttpResponse objects like normal Django
        # views is the easiest way to accomplish that.
        return SafeString(self.view(request).content.decode('utf-8'))
