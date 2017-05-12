import ast
from pathlib import Path
from django.utils.safestring import SafeString

try:
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.lexers.templates import HtmlDjangoLexer
    from pygments.formatters import HtmlFormatter
except ImportError:
    highlight = None

APP_DIR = Path(__file__).resolve().parent
PY_DIR = APP_DIR / 'examples'
TEMPLATES_DIR = APP_DIR / 'templates' / 'examples'


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


def clean_python_source(source):
    '''
    Remove the leading docstring from the given source code.
    '''

    mod = ast.parse(source)
    first_non_docstring = mod.body[1]
    return '\n'.join(source.splitlines()[first_non_docstring.lineno - 1:])


def clean_template_source(source):
    '''
    Remove any un-indented {% include %} tags in the given template source.
    '''

    return '\n'.join(
        line for line in source.splitlines()
        if not line.startswith(r'{% include')
    )


def render_template_source(filename):
    with open(str(TEMPLATES_DIR / filename)) as f:
        return render_source(clean_template_source(f.read()), 'html+django')


def render_python_source(filename):
    with open(str(PY_DIR / filename)) as f:
        return render_source(clean_python_source(f.read()), 'python')
