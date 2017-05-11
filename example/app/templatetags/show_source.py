from pathlib import Path
from django import template
from django.utils.safestring import SafeString

try:
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.lexers.templates import HtmlDjangoLexer
    from pygments.formatters import HtmlFormatter
except ImportError:
    highlight = None

MY_DIR = Path(__file__).resolve().parent
APP_DIR = MY_DIR.parent
PY_DIR = APP_DIR / 'examples'
TEMPLATES_DIR = APP_DIR / 'templates' / 'examples'

register = template.Library()


def render_source(contents, filetype):
    if highlight is None:
        return contents
    else:
        formatter = HtmlFormatter(noclasses=True, style='trac')
        if filetype == 'html+django':
            lexer = HtmlDjangoLexer()
        elif filetype == 'python':
            lexer = PythonLexer()
        else:
            raise ValueError('unknown filetype: {}'.format(filetype))
        return SafeString(highlight(contents, lexer, formatter))


@register.simple_tag(takes_context=True)
def show_template_source(context, filename):
    with open(str(TEMPLATES_DIR / filename)) as f:
        return render_source(f.read(), 'html+django')


@register.simple_tag(takes_context=True)
def show_python_source(context, filename):
    with open(str(PY_DIR / filename)) as f:
        return render_source(f.read(), 'python')
