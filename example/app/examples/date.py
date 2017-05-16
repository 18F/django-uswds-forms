'''
Date

This example shows how to render a date input using a
uswds_forms.UswdsDateField.
'''

from django.shortcuts import render
import uswds_forms


class MyForm(uswds_forms.UswdsForm):
    date = uswds_forms.UswdsDateField(label="What is your favorite date?")


def view(request):
    return render(request, 'examples/date.html', {
        'form': MyForm() if request.method == 'GET' else MyForm(request.POST)
    })
