from django.shortcuts import render
from collections import OrderedDict

from .example import Example

EXAMPLE_NAMES = [
    'everything',
]

EXAMPLES = OrderedDict([(name, Example(name)) for name in EXAMPLE_NAMES])


def home(request):
    example = EXAMPLES['everything']

    return render(request, 'home.html', {
        'EXAMPLES': EXAMPLES,
        'rendered_example': example.render(request),
        'example': example,
    })
