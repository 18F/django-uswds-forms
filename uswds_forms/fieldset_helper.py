from django import forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.safestring import SafeString
from django.template.loader import render_to_string

from . import date


__all__ = (
    'fieldset',
)

# The template path for a <fieldset> wrapping a form input. It
# should exist for all supported template engines.
TEMPLATE_NAME = 'uswds_forms/fieldset.html'

# These are widget classes that consist of multiple sub-widgets. We'd
# like to use a <legend> element with these, instead of a <label>, so
# that screen-readers contextualize them properly.
LEGEND_WIDGETS = (
    date.UswdsDateWidget,
    forms.CheckboxSelectMultiple,
    forms.RadioSelect
)


def get_context(field):
    '''
    Get the context for the fieldset template, regardless of template
    engine backend, and return it.
    '''

    use_legend = isinstance(field.field.widget, LEGEND_WIDGETS)

    label_attrs = {}

    if field.errors:
        label_attrs['class'] = 'usa-input-error-label'

    if use_legend:
        aria_hidden_label_tag = create_aria_hidden_label_tag(
            field,
            label_attrs
        )
    else:
        aria_hidden_label_tag = None

    label_tag = field.label_tag(attrs=label_attrs)

    return {
        'field': field,
        'put_field_before_label': isinstance(field.field.widget,
                                             forms.CheckboxInput),
        'use_legend': use_legend,
        'aria_hidden_label_tag': aria_hidden_label_tag,
        'label_tag': label_tag,
    }


def fieldset(field):
    '''
    Render the given bound field as a ``<fieldset>``. The field’s label
    is also rendered, along with any associated form errors and help text.

    .. highlight:: html+django

    Once added to a Jinja2 environment, this function can be used
    from Jinja2 templates like so::

        {{ fieldset(my_form.name) }}
        {{ fieldset(my_form.address) }}
        {{ fieldset(my_form.birthday) }}
    '''

    return SafeString(render_to_string(TEMPLATE_NAME, get_context(field)))


def create_aria_hidden_label_tag(field, attrs):
    '''
    A <label> for sighted users only.

    Sighted users will see this instead of <legend> for groups of
    sub-widgets because it's easier to visually style.

    It can't include a 'for' attribute because the attribute will
    likely be duplicated in the sub-widget grouping, which can
    confuse browsers because multiple labels for the same id will
    exist.

    Other than that, much of this code is taken from Django's
    implementation of BoundField.label_tag().
    '''

    attrs = {'aria_hidden': 'true', **attrs}
    if field.field.required and hasattr(field.form, 'required_css_class'):
        if 'class' in attrs:
            attrs['class'] += ' ' + field.form.required_css_class
        else:
            attrs['class'] = field.form.required_css_class
    attrs = flatatt(attrs)
    return SafeString(format_html('<label{}>{}</label>', attrs, field.label))
