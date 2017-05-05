from django import forms
from django.utils.html import format_html


class UswdsWidgetMixin:
    # Note that we're only specifying this to ensure that we
    # get the fix for https://code.djangoproject.com/ticket/28059,
    # which allows us to specify custom classes for <ul>'s.
    #
    # Once that fix makes it into a stable Django release, we can
    # remove this line and its associated template file.
    template_name = 'uswds_forms/multiple_input.html'

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


class UswdsCheckbox(UswdsWidgetMixin, forms.widgets.CheckboxSelectMultiple):
    pass
