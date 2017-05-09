from django import forms
from django.template.loader import render_to_string

from .errors import UswdsErrorList


__all__ = (
    'UswdsForm',
)


class UswdsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'error_class' not in kwargs:
            kwargs['error_class'] = UswdsErrorList
        super().__init__(*args, **kwargs)

    def as_fieldsets(self):
        return render_to_string('uswds_forms/form_as_fieldsets.html', {
            'form': self,
        })
