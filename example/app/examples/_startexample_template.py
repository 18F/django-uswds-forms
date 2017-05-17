'''
TODO: Put example name here.

TODO: Put example description here.
'''

from django.shortcuts import render
from django import forms
import uswds_forms


class MyForm(uswds_forms.UswdsForm):
    president = forms.ChoiceField(
        label="Example form field",
        widget=uswds_forms.UswdsRadioSelect,
        choices=(
            ('a', 'Choice A'),
            ('b', 'Choice B'),
        )
    )


def view(request):
    return render(request, 'examples/new_example_template.html', {
        'form': MyForm() if request.method == 'GET' else MyForm(request.POST)
    })
