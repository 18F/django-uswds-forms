from uswds_forms.errors import UswdsErrorList


def test_errors_work():
    errors = UswdsErrorList(['<i>hi</i>'])
    assert str(errors) == (
        '<ul class="usa-unstyled-list">'
        '<li class="usa-input-error-message" role="alert">'
        '&lt;i&gt;hi&lt;/i&gt;'
        '</li>'
        '</ul>'
    )
