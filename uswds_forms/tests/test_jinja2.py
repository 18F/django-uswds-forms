from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent
JINJA2_DIR = APP_DIR / 'jinja2' / 'uswds_forms'
TEMPLATES_DIR = APP_DIR / 'templates' / 'uswds_forms'


def test_date_template_is_identical():
    '''
    This template uses the subset of syntax shared by Jinja2 and
    Django Templates, so the two versions of it should be identical.
    '''

    assert (JINJA2_DIR / 'date.html').read_text() == \
           (TEMPLATES_DIR / 'date.html').read_text()


def test_input_option_template_is_identical():
    '''
    This template uses the subset of syntax shared by Jinja2 and
    Django Templates, so the two versions of it should be identical.
    '''

    assert (JINJA2_DIR / 'input_option.html').read_text() == \
           (TEMPLATES_DIR / 'input_option.html').read_text()
