from django import forms
from django.template.loader import render_to_string

from .errors import UswdsErrorList


__all__ = (
    'UswdsForm',
)


class UswdsForm(forms.Form):
    '''
    This is a subclass of :class:`django.forms.Form` that provides
    some functionality for rendering USWDS forms. Its constructor
    takes the exact same arguments.

    By default, it will use :class:`uswds_forms.UswdsErrorList` to
    display errors.
    '''

    def __init__(self, *args, **kwargs):
        if 'error_class' not in kwargs:
            kwargs['error_class'] = UswdsErrorList
        super().__init__(*args, **kwargs)

    def as_fieldsets(self):
        '''
        Like other convenience methods such as
        :py:meth:`~django.forms.Form.as_p` and
        :py:meth:`~django.forms.Form.as_table`, this method renders all
        the form's fields as a series of ``<fieldset>`` elements.
        '''

        return render_to_string('uswds_forms/form_as_fieldsets.html', {
            'form': self,
        })
