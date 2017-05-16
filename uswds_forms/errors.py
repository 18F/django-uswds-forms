from django.forms.utils import ErrorList
from django.utils.html import format_html, format_html_join

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

    def as_ul(self):
        # Note that because we're a subclass of list, we're basically
        # just testing to see if we're an empty list here.
        if not self:
            return ''

        return format_html(
            '<ul class="usa-unstyled-list">{}</ul>',
            format_html_join(
                '',
                '<li class="usa-input-error-message" role="alert">{}</li>',
                ((e,) for e in self)
            )
        )
