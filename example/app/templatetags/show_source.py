from pathlib import Path
from django import template
from django.utils.safestring import SafeString
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.templates import HtmlDjangoLexer
from pygments.formatters import HtmlFormatter

MY_DIR = Path(__file__).resolve().parent
APP_DIR = MY_DIR.parent
PY_DIR = APP_DIR / 'examples'
TEMPLATES_DIR = APP_DIR / 'templates' / 'examples'

register = template.Library()


def get_formatter():
    return HtmlFormatter(noclasses=True, style='trac')


@register.simple_tag(takes_context=True)
def show_template_source(context, filename):
    with open(str(TEMPLATES_DIR / filename)) as f:
        return SafeString(highlight(f.read(), HtmlDjangoLexer(),
                          get_formatter()))


@register.simple_tag(takes_context=True)
def show_python_source(context, filename):
    with open(str(PY_DIR / filename)) as f:
        return SafeString(highlight(f.read(), PythonLexer(),
                          get_formatter()))
