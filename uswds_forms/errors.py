from django.forms.utils import ErrorList
from django.template.loader import render_to_string


__all__ = (
    'UswdsErrorList',
)


class UswdsErrorList(ErrorList):
    '''
    This is an error list formatter that renders errors in the style used
    by USWDS forms. For an example of how this makes errors look in
    practice, see the `USWDS text inputs example
    <https://standards.usa.gov/components/form-controls/#text-input>`_.

    Note that you probably don't need to use this class directly, as 
    :class:`~uswds_forms.UswdsForm` uses it by default.

    For more details on how to use this class, see the Django
    documentation on `customizing the error list format <https://docs.djangoproject.com/en/1.11/ref/forms/api/#customizing-the-error-list-format>`_.
    '''

    def __str__(self):
        return self.as_html()

    def as_html(self):
        # No idea what this line is for, but it's shown in sample code:
        # https://docs.djangoproject.com/en/1.11/ref/forms/api/
        if not self:
            return ''

        return render_to_string('uswds_forms/errors.html', {
            'errors': self
        })
