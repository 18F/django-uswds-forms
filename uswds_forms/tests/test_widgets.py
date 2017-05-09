import datetime
from django import forms

from uswds_forms.date import UswdsDateWidget
from uswds_forms import UswdsCheckboxSelectMultiple, UswdsRadioSelect


def test_date_widget_decompress():
    w = UswdsDateWidget()
    d = datetime.date(2017, 5, 4)
    assert w.decompress(d) == [2017, 5, 4]


def test_checkbox_select_multiple_uses_unstyled_list():
    class MyForm(forms.Form):
        checkboxes = forms.MultipleChoiceField(
            widget=UswdsCheckboxSelectMultiple,
            choices=(('one', 'One'), ('two', 'Two')),
        )

    # Note that this will fail if Django < 1.11.1!
    assert 'usa-unstyled-list' in MyForm().as_p()


def test_radio_select_uses_unstyled_list():
    class MyForm(forms.Form):
        radios = forms.ChoiceField(
            widget=UswdsRadioSelect,
            choices=(('one', 'One'), ('two', 'Two')),
        )

    # Note that this will fail if Django < 1.11.1!
    assert 'usa-unstyled-list' in MyForm().as_p()
