from django import forms
from django.utils.html import format_html


class IdRequiredWidget:
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if 'id' not in context['widget']['attrs']:
            raise ValueError('USWDS-style inputs must have "id" '
                             'attributes')
        return context

class UswdsRadioSelect(IdRequiredWidget, forms.widgets.RadioSelect):
    option_template_name = 'uswds_forms/input_option.html'

class UswdsCheckbox(IdRequiredWidget,
                    forms.widgets.CheckboxSelectMultiple):
    option_template_name = 'uswds_forms/input_option.html'
