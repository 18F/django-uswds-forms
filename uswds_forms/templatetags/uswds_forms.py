from django import template, forms
from .. import date


register = template.Library()


# These are widget classes that consist of multiple sub-widgets. We'd
# like to use a <legend> element with these, instead of a <label>, so
# that screen-readers contextualize them properly.
LEGEND_WIDGETS = (
    date.UswdsSplitDateWidget,
    forms.CheckboxSelectMultiple,
    forms.RadioSelect
)


@register.simple_tag(takes_context=True)
def fieldset(context, field):
    '''
    This template tag makes it easy to render form fields as
    <fieldset> elements.
    '''

    t = context.template.engine.get_template('uswds_forms/fieldset.html')

    use_legend = isinstance(field.field.widget, LEGEND_WIDGETS)

    if use_legend:
        aria_hidden_label_tag = field.label_tag(attrs={
            'aria-hidden': 'true',
        })
    else:
        aria_hidden_label_tag = None

    return t.render(template.Context({
        'field': field,
        'put_field_before_label': isinstance(field.field.widget,
                                             forms.CheckboxInput),
        'use_legend': use_legend,
        'aria_hidden_label_tag': aria_hidden_label_tag,
    }))
