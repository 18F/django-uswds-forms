from django import forms

from .errors import UswdsErrorList


class UswdsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        if 'error_class' not in kwargs:
            kwargs['error_class'] = UswdsErrorList
        super().__init__(*args, **kwargs)
