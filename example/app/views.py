from django.http import HttpResponseNotFound
from django.shortcuts import render
from collections import OrderedDict

from .example import Example

EXAMPLE_NAMES = [
    'everything',
]

EXAMPLES = OrderedDict([(name, Example(name)) for name in EXAMPLE_NAMES])


def ctx(**kwargs):
    return {
        'EXAMPLES': EXAMPLES,
        **kwargs
    }


def example(request, name):
    example = EXAMPLES.get(name)

    if example is None:
        return HttpResponseNotFound('Example not found.')

    return render(request, 'example.html', ctx(
        rendered_example=example.render(request),
        example=example,
    ))


def home(request):
    return render(request, 'home.html', ctx())
