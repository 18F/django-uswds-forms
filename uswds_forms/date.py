from datetime import date
from collections import namedtuple

from django.core.exceptions import ValidationError
from django.forms import MultiWidget, NumberInput
from django.forms.fields import MultiValueField, IntegerField

FieldNames = namedtuple('FieldNames', ['year', 'month', 'day'])


class ExtraValidationNumberInput(NumberInput):
    '''
    NumberInput with extra HTML5 validation attributes.
    '''

    extra_validation_attrs = {}

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx['widget']['attrs'].update(self.extra_validation_attrs)
        return ctx


class MonthInput(ExtraValidationNumberInput):
    '''
    NumberInput with extra HTML5 validation attrs for numeric months.
    '''

    extra_validation_attrs = {
        'pattern': r'0?[1-9]|1[012]',
        'min': '1',
        'max': '12',
    }


class YearInput(ExtraValidationNumberInput):
    '''
    NumberInput with extra HTML5 validation attrs for 4-digit years.
    '''

    extra_validation_attrs = {
        'pattern': r'[0-9]{4}',
        'min': '1900',
        'max': '9999',
    }


class DayInput(ExtraValidationNumberInput):
    '''
    NumberInput with extra HTML5 validation attrs for day-of-month.
    '''

    extra_validation_attrs = {
        'pattern': r'0?[1-9]|1[0-9]|2[0-9]|3[01]',
        'min': '1',
        'max': '31',
    }


class SplitDateWidget(MultiWidget):
    '''
    A widget for a USWDS-style date, with separate number fields for
    date, month, and year.

    The widget is expected to be in a <fieldset>. Instead of a <label>,
    the label should be rendered inside a <legend>.
    '''

    template_name = 'uswds_forms/date.html'

    def __init__(self, attrs=None):
        widgets = (
            YearInput(attrs=attrs),
            MonthInput(attrs=attrs),
            DayInput(attrs=attrs),
        )
        super().__init__(widgets, attrs=attrs)

    def decompress(self, value):
        if value:
            return [value.year, value.month, value.day]
        return [None, None, None]

    @staticmethod
    def get_field_names(name):
        # Note that this is actually dependent on the way our superclass
        # names our subwidgets. The naming scheme should be pretty stable,
        # though.
        return FieldNames(year=name + '_0', month=name + '_1', day=name + '_2')

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        widget = ctx['widget']
        hint_id = '%s_%s' % (widget['attrs']['id'], 'hint')
        for subwidget in widget['subwidgets']:
            subwidget['attrs'].update({
                'class': 'usa-input-inline',
                'aria-describedby': hint_id,
            })
        year, month, day = widget['subwidgets']
        ctx['widget'].update(dict(
            hint_id=hint_id,
            year=year,
            month=month,
            day=day
        ))
        return ctx


class SplitDateField(MultiValueField):
    '''
    A field for a USWDS-style date.
    '''

    widget = SplitDateWidget

    def __init__(self, *args, **kwargs):
        fields = (
            IntegerField(),
            IntegerField(),
            IntegerField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            year, month, day = data_list
            try:
                return date(year, month, day)
            except ValueError as e:
                raise ValidationError('Invalid date: %s.' % str(e))
        return None
