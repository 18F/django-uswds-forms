from django.forms.utils import ErrorList
from django.template.loader import render_to_string


__all__ = (
    'UswdsErrorList',
)


class UswdsErrorList(ErrorList):
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
