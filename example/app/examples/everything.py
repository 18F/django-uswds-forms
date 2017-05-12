'''
The kitchen sink

This example combines almost every feature of django-uswds-forms
into one big form.
'''

from django.shortcuts import render
from django import forms
import uswds_forms


class EverythingForm(uswds_forms.UswdsForm):
    required_css_class = 'usa-input-required'

    president = forms.ChoiceField(
        label="Who is your favorite president?",
        widget=uswds_forms.UswdsRadioSelect,
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

    states = uswds_forms.UswdsMultipleChoiceField(
        label="What states have you visited?",
        required=False,
        choices=(
            ('OH', 'Ohio'),
            ('IL', 'Illinois'),
            ('CA', 'California'),
        )
    )

    date = uswds_forms.UswdsDateField(
        label="What is your favorite date?"
    )

    trigger_non_field_error = forms.BooleanField(
        label=("After submitting this form, trigger a "
               "non-field error."),
        required=False,
    )


def view(request):
    if request.method == 'POST':
        form = EverythingForm(request.POST)
        if form.data.get('trigger_non_field_error'):
            form.add_error(None, 'This is the non-field error you requested.')
    else:
        form = EverythingForm()

    return render(request, 'examples/everything.html', {
        'form': form
    })
