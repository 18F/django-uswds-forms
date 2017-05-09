from django import forms


__all__ = (
    'UswdsRadioSelect',
    'UswdsCheckboxSelectMultiple',
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
