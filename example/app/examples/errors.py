'''
Errors

This example shows how errors are automatically given proper styling,
thanks to uswds_forms.UswdsForm and Django 1.11's new form rendering API.
'''

from django.shortcuts import render
from django import forms
import uswds_forms


class MyForm(uswds_forms.UswdsForm):
    text = forms.CharField(label="Text input label")

    checkbox = forms.BooleanField(label='I agree to the terms of service')

    def clean(self):
        super().clean()
        self.add_error('text', 'Helpful error message #1')
        self.add_error('text', 'Helpful error message #2')
        self.add_error(None, 'Helpful non-field error message #1')
        self.add_error(None, 'Helpful non-field error message #2')

def view(request):
    # Since this example is specifically made to show errors, we'll
    # "simulate" a POST request here.

    form = MyForm({'text': 'blah'})
    form.is_valid()
    return render(request, 'examples/errors.html', {'form': form})
