from django import template

from ..fieldset_helper import TEMPLATE_NAME, get_context

register = template.Library()


@register.simple_tag(takes_context=True)
def fieldset(context, field):
    '''
    This template tag makes it easy to render form fields as
    <fieldset> elements.
    '''

    t = context.template.engine.get_template(TEMPLATE_NAME)

    return t.render(template.Context(get_context(field)))
