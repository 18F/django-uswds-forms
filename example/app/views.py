from django.shortcuts import render
from django import forms
from uswds_forms.radio_and_checkbox import (
    UswdsRadioSelect,
    UswdsCheckboxSelectMultiple
)
from uswds_forms.date import SplitDateField
from uswds_forms.errors import UswdsErrorList


class ExampleForm(forms.Form):
    required_css_class = 'usa-input-required'

    president = forms.ChoiceField(
        label="Who is your favorite president?",
        widget=UswdsRadioSelect,
        help_text=("If you don't see your favorite, just pick your "
                   "favorite of the ones we've listed."),
        choices=(
            ('washington', 'George Washington'),
            ('adams', 'John Adams'),
            ('jefferson', 'Thomas Jefferson'),
        )
    )

    park = forms.CharField(
        label=("If you could choose the name of the next national park, "
               "what would it be?"),
        help_text='Note that "Parky McParkface" is not a valid response.'
    )

    states = forms.MultipleChoiceField(
        label="What states have you visited?",
        widget=UswdsCheckboxSelectMultiple,
        required=False,
        choices=(
            ('OH', 'Ohio'),
            ('IL', 'Illinois'),
            ('CA', 'California'),
        )
    )

    date = SplitDateField(label="What is your favorite date?")

    trigger_non_field_error = forms.BooleanField(
        label=("After submitting this form, trigger a "
               "non-field error."),
        required=False,
    )


def home(request):
    form_kwargs = dict(
        error_class=UswdsErrorList
    )

    if request.method == 'POST':
        form = ExampleForm(request.POST, **form_kwargs)
        if form.data.get('trigger_non_field_error'):
            form.add_error(None, 'This is the non-field error you requested.')
    else:
        form = ExampleForm(**form_kwargs)

    return render(request, 'home.html', {
        'form': form
    })
