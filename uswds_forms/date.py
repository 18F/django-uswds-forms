from datetime import date
from collections import namedtuple

from django.core.exceptions import ValidationError
from django.forms import MultiWidget, NumberInput
from django.forms.fields import MultiValueField, IntegerField


__all__ = (
    'UswdsDateField',
    'UswdsDateWidget',
)


# This is just a convenience that allows us to reference the
# fields without having to remember what index they are in the
# tuple ordering.
DateTuple = namedtuple('DateTuple', ['year', 'month', 'day'])


FIELD_ORDERING = DateTuple._fields
YEAR_ID = FIELD_ORDERING.index('year')
MONTH_ID = FIELD_ORDERING.index('month')
DAY_ID = FIELD_ORDERING.index('day')


class UswdsDateWidget(MultiWidget):
    '''
    A :class:`django.forms.MultiWidget` for a USWDS-style date, with
    separate number fields for date, month, and year.

    This widget is used automatically by
    :class:`uswds_forms.UswdsDateField`, so you probably won't need
    to use it directly. However, it can be subclassed in case you need
    to customize it.
    '''

    #: This is the default template used by the widget, which can
    #: be overridden if needed.
    template_name = 'uswds_forms/date.html'

    year_attrs = {
        'pattern': r'[0-9]{4}',
        'min': '1900',
        'max': '9999',
    }

    month_attrs = {
        'pattern': r'0?[1-9]|1[012]',
        'min': '1',
        'max': '12',
    }

    day_attrs = {
        'pattern': r'0?[1-9]|1[0-9]|2[0-9]|3[01]',
        'min': '1',
        'max': '31',
    }

    def __init__(self, attrs=None):
        widgets = DateTuple(
            year=NumberInput(attrs=self.year_attrs),
            month=NumberInput(attrs=self.month_attrs),
            day=NumberInput(attrs=self.day_attrs),
        )
        super().__init__(widgets, attrs=attrs)

    def decompress(self, value):
        if value:
            return list(DateTuple(
                year=value.year,
                month=value.month,
                day=value.day
            ))
        return [None, None, None]

    @staticmethod
    def get_field_names(name):
        # Note that this is actually dependent on the way our superclass
        # names our subwidgets. The naming scheme should be pretty stable,
        # though.
        return DateTuple(
            year=name + '_{}'.format(YEAR_ID),
            month=name + '_{}'.format(MONTH_ID),
            day=name + '_{}'.format(DAY_ID)
        )

    def get_context(self, name, value, attrs):
        '''
        Returns the context for the widget's template. This returns
        a superset of what's provided by its superclass'
        :meth:`~django.forms.MultiWidget.get_context`
        implementation, adding the following keys to ``widget``:

        * ``'hint_id'``: The unique id of some hint text showing users
          an example of what they can enter.

        * ``'subwidgets'``: This has the same iterable value described
          in the superclass documentation, but it has been enhanced
          such that its ``year``, ``month``, and ``day`` properties are
          aliases to its entries. Using these aliases can potentially make
          templates more readable.
        '''

        ctx = super().get_context(name, value, attrs)
        widget = ctx['widget']
        hint_id = '%s_%s' % (widget['attrs']['id'], 'hint')
        for subwidget in widget['subwidgets']:
            subwidget['attrs'].update({
                'class': 'usa-input-inline',
                'aria-describedby': hint_id,
            })
        widget['subwidgets'] = DateTuple(*widget['subwidgets'])
        widget.update({'hint_id': hint_id})
        return ctx


class UswdsDateField(MultiValueField):
    '''
    A :class:`django.forms.MultiValueField` for a USWDS-style date.
    Its value normalizes to a Python :class:`datetime.date` object.

    For an example of how this looks in practice, see the
    `USWDS date input example
    <https://standards.usa.gov/components/form-controls/#date-input>`_.
    '''

    widget = UswdsDateWidget

    def __init__(self, *args, **kwargs):
        fields = DateTuple(
            year=IntegerField(),
            month=IntegerField(),
            day=IntegerField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            fields = DateTuple(*data_list)
            try:
                return date(
                    year=fields.year,
                    month=fields.month,
                    day=fields.day
                )
            except ValueError as e:
                raise ValidationError('Invalid date: %s.' % str(e))
        return None
