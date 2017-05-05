from django.shortcuts import render
from django import forms
from uswds_forms.radio_and_checkbox import UswdsRadioSelect, UswdsCheckbox
from uswds_forms.date import SplitDateField
from uswds_forms.errors import UswdsErrorList


class ExampleForm(forms.Form):
    president = forms.ChoiceField(
        label="Who is your favorite president?",
        widget=UswdsRadioSelect,
        help_text=("If you don't see your favorite, just pick your "
                   "favorite of the ones we've listed."),
        choices=(
            ('george', 'George Washington'),
            ('john', 'John Adams'),
            ('thomas', 'Thomas Jefferson'),
        )
    )

    states = forms.MultipleChoiceField(
        label="What states have you visited?",
        widget=UswdsCheckbox,
        choices=(
            ('oh', 'Ohio'),
            ('il', 'Illinois'),
            ('ca', 'California'),
        )
    )

    date = SplitDateField(label="What is your favorite date?")


def home(request):
    form_kwargs = dict(
        error_class=UswdsErrorList
    )

    if request.method == 'POST':
        form = ExampleForm(request.POST, **form_kwargs)
    else:
        form = ExampleForm(**form_kwargs)

    return render(request, 'home.html', {
        'form': form
    })
