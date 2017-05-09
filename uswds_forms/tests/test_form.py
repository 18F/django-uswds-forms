from django import forms

from uswds_forms.form import UswdsForm


def test_as_fieldsets_works():
    class MyForm(UswdsForm):
        my_field = forms.CharField(label="my field", help_text="my help")

    form = MyForm()
    html = form.as_fieldsets()

    assert '<input' in html
    assert 'my field' in html
    assert 'my help' in html
