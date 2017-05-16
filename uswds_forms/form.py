from django import forms
from django.utils.safestring import SafeString

from .fieldset_helper import fieldset
from .errors import UswdsErrorList


__all__ = (
    'UswdsForm',
)


class UswdsForm(forms.Form):
    '''
    This is a subclass of :class:`django.forms.Form` that provides
    some functionality for rendering USWDS forms. Its constructor
    takes the exact same arguments, but some defaults are
    changed:

    * ``error_class`` defaults to :class:`uswds_forms.UswdsErrorList`,
      so that errors are formatted nicely.

    * :py:attr:`~django.forms.Form.label_suffix` defaults to the
      empty string, since none of the USWDS example forms have
      colons after the label names.
    '''

    def __init__(self, *args, **kwargs):
        if 'error_class' not in kwargs:
            kwargs['error_class'] = UswdsErrorList
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    def as_fieldsets(self):
        '''
        Like other convenience methods such as
        :py:meth:`~django.forms.Form.as_p` and
        :py:meth:`~django.forms.Form.as_table`, this method renders all
        the form's fields as a series of ``<fieldset>`` elements.

        Under the hood, this just iterates over the form's fields and
        renders them via the
        :ref:`fieldset template tag <fieldset-template-tag>`, so you
        can use that if you need more granular control over rendering.
        '''

        return SafeString('\n'.join([fieldset(field) for field in self]))
