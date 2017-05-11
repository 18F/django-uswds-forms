from django.shortcuts import render
from django.utils.safestring import SafeString

from .examples import everything


def home(request):
    # This is sort of weird because we're decoding the
    # content in a HttpResponse; it's not an ideal API,
    # but we want the examples be as conventional as
    # possible so they don't confuse readers, and having
    # them return HttpResponse objects like normal Django
    # views is the easiest way to accomplish that.
    html = everything.view(request).content.decode('utf-8')

    rendered_example = SafeString(html)

    return render(request, 'home.html', {
        'rendered_example': rendered_example,
    })
