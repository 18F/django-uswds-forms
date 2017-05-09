from django import forms


__all__ = (
    'UswdsRadioSelect',
    'UswdsCheckboxSelectMultiple',
    'UswdsMultipleChoiceField',
)


class UswdsWidgetMixin:
    option_template_name = 'uswds_forms/input_option.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        widget_attrs = context['widget']['attrs']
        if 'class' not in widget_attrs:
            widget_attrs['class'] = 'usa-unstyled-list'
        if 'id' not in widget_attrs:
            raise ValueError('USWDS-style inputs must have "id" '
                             'attributes')
        return context


class UswdsRadioSelect(UswdsWidgetMixin, forms.widgets.RadioSelect):
    pass


class UswdsCheckboxSelectMultiple(UswdsWidgetMixin,
                                  forms.widgets.CheckboxSelectMultiple):
    pass


class UswdsMultipleChoiceField(forms.fields.MultipleChoiceField):
    '''
    This is just a Django `MultipleChoiceField` with the
    `UswdsCheckboxSelectMultiple` widget. Easier than having to
    specify the widget manually, and provided for convenience because
    the usability of the default `SelectMultiple` is so terrible
    that you'll never want to use it.
    '''

    widget = UswdsCheckboxSelectMultiple
