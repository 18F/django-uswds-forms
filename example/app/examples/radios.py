'''
Radio buttons

This example shows how to render radio buttons using the
uswds_forms.UswdsRadioSelect widget.
'''

from django.shortcuts import render
from django import forms
import uswds_forms


class MyForm(uswds_forms.UswdsForm):
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


def view(request):
    return render(request, 'examples/radios.html', {
        'form': MyForm() if request.method == 'GET' else MyForm(request.POST)
    })
