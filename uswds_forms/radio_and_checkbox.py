from django import forms


__all__ = (
    'UswdsRadioSelect',
    'UswdsCheckboxSelectMultiple',
    'UswdsMultipleChoiceField',
)


class UswdsWidgetMixin:
    option_template_name = 'uswds_forms/input_option.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)  # type: ignore
        widget_attrs = context['widget']['attrs']
        if 'class' not in widget_attrs:
            widget_attrs['class'] = 'usa-unstyled-list'
        if 'id' not in widget_attrs:
            raise ValueError('USWDS-style inputs must have "id" '
                             'attributes')
        return context


class UswdsRadioSelect(UswdsWidgetMixin, forms.widgets.RadioSelect):
    '''
    This subclass of :class:`django.forms.RadioSelect` styles
    radio buttons appropriately for USWDS.

    You can use this in a :class:`django.forms.ChoiceField` to get a list
    of radio buttons instead of a ``<select>`` element for your
    choices.

    For an example of how this looks in practice, see the
    `USWDS radio buttons example
    <https://standards.usa.gov/components/form-controls/#radio-buttons>`_.
    '''


class UswdsCheckboxSelectMultiple(UswdsWidgetMixin,
                                  forms.widgets.CheckboxSelectMultiple):
    '''
    This subclass of :class:`django.forms.CheckboxSelectMultiple` styles
    grouped checkboxes appropriately for USWDS.

    You can use this in a :class:`django.forms.MultipleChoiceField` to
    get a list of checkboxes instead of a ``<select multiple>`` element
    for your choices.

    For an example of how this looks in practice, see the
    `USWDS checkboxes example
    <https://standards.usa.gov/components/form-controls/#checkboxes>`_.
    '''


class UswdsMultipleChoiceField(forms.fields.MultipleChoiceField):
    '''
    This is just a :class:`django.forms.MultipleChoiceField`
    that uses the :class:`~uswds_forms.UswdsCheckboxSelectMultiple` widget.

    We've provided this field for convenience because
    the usability of the default :class:`django.forms.SelectMultiple`
    is so terrible that you'll probably never want to use it. `Burn
    your select tags! <https://www.youtube.com/watch?v=CUkMCQR4TpY>`_
    '''

    widget = UswdsCheckboxSelectMultiple
