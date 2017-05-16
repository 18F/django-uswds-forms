from jinja2 import Environment
import uswds_forms


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'fieldset': uswds_forms.fieldset,
    })
    return env
