from datetime import date
from collections import namedtuple

from django.core.exceptions import ValidationError
from django.forms import MultiWidget, NumberInput
from django.forms.fields import MultiValueField, IntegerField
from django.template.loader import render_to_string


FieldNames = namedtuple('FieldNames', ['year', 'month', 'day'])


class SplitDateWidget(MultiWidget):
    '''
    A widget for a USWDS-style date, with separate number fields for
    date, month, and year.

    The widget is expected to be in a <fieldset>. Instead of a <label>,
    the label should be rendered inside a <legend>.
    '''

    def __init__(self, attrs=None):
        widgets = (
            NumberInput(),
            NumberInput(),
            NumberInput(),
        )
        super().__init__(widgets, attrs=attrs)

    def decompress(self, value):
        if value:
            return [value.year, value.month, value.day]
        return [None, None, None]

    @staticmethod
    def get_field_names(name):
        return FieldNames(year=name + '_0', month=name + '_1', day=name + '_2')

    def render(self, name, value, attrs=None):
        # Django MultiWidget rendering is not particularly well-suited to
        # what we want to do, so we'll have to override it here. Much
        # of this code is copied from MultiWidget.render(), unfortunately.

        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, list):
            value = self.decompress(value)

        final_attrs = self.build_attrs(self.attrs, attrs)
        id_ = final_attrs.get('id')
        widget_infos = []
        for i, widget in enumerate(self.widgets):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None

            # Note that we're never calling our sub-widgets'
            # render() method, and that's ok. We're really just defining
            # our widgets to plug into Django's MultiValueField/MultiWidget
            # architecture; our template will be rendering the sub-widgets
            # itself.

            widget_infos.append({
                'id': '%s_%s' % (id_, i),
                'name': name + '_%s' % i,
                'value': widget_value or ''
            })

        year, month, day = widget_infos

        # TODO: This widget was originally created for pre-Django 1.11
        # style widgets, so it's doing its own rendering. We should
        # probably modify it to use a passed-in renderer, or whatever
        # the proper Django 1.11 way of doing things is.

        return render_to_string('uswds_forms/date.html', {
            'hint_id': '%s_%s' % (id_, 'hint'),
            'year': year,
            'month': month,
            'day': day,
        })


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
