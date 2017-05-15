from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent
JINJA2_DIR = APP_DIR / 'jinja2' / 'uswds_forms'
TEMPLATES_DIR = APP_DIR / 'templates' / 'uswds_forms'


def assert_templates_are_identical(name):
    '''
    Some of our templates use the subset of syntax shared by Jinja2 and
    Django Templates, so the two versions of it should be identical.

    Note that this assertion is currently here to ensure that either
    backend doesn't lag behind the other; however, if a real need
    arises for the templates to diverge, tests using this assertion
    can be removed.
    '''

    assert (JINJA2_DIR / name).read_text() == \
           (TEMPLATES_DIR / name).read_text()


def test_date_template_is_identical():
    assert_templates_are_identical('date.html')


def test_input_option_template_is_identical():
    assert_templates_are_identical('input_option.html')


def test_fieldset_template_is_identical():
    assert_templates_are_identical('fieldset.html')
