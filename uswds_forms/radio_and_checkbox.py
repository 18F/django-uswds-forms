from django import forms
from django.utils.html import format_html

from .config import USE_NEW_FORM_API

if not USE_NEW_FORM_API:
    class LabelInputSiblingRenderer():
        def render(self, name=None, value=None, attrs=None):
            # This is mostly just a copy-paste of our superclass method, it
            # just tweaks the HTML structure to be USWDS-friendly.
            if self.id_for_label:
                label_for = format_html(' for="{}"', self.id_for_label)
            else:
                raise ValueError('USWDS-style inputs must have "id" '
                                 'attributes')
            attrs = dict(self.attrs, **attrs) if attrs else self.attrs
            return format_html(
                '{}<label{}>{}</label>', self.tag(attrs), label_for,
                self.choice_label,
            )

    class UswdsCheckboxInput(LabelInputSiblingRenderer,
                             forms.widgets.CheckboxChoiceInput):
        pass

    class UswdsRadioChoiceInput(LabelInputSiblingRenderer,
                                forms.widgets.RadioChoiceInput):
        pass

    class UswdsRadioFieldRenderer(forms.widgets.ChoiceFieldRenderer):
        choice_input_class = UswdsRadioChoiceInput

    class UswdsRadioSelect(forms.widgets.RadioSelect):
        renderer = UswdsRadioFieldRenderer

    class UswdsCheckboxFieldRenderer(forms.widgets.ChoiceFieldRenderer):
        choice_input_class = UswdsCheckboxInput

    class UswdsCheckbox(forms.widgets.CheckboxSelectMultiple):
        renderer = UswdsCheckboxFieldRenderer
else:
    # We're using the new form API, which makes this easier.

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
