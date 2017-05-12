from django.shortcuts import render
from django.utils.safestring import SafeString

from .examples import everything
from .render_source import render_template_source, render_python_source


def home(request):
    # This is sort of weird because we're decoding the
    # content in a HttpResponse; it's not an ideal API,
    # but we want the examples be as conventional as
    # possible so they don't confuse readers, and having
    # them return HttpResponse objects like normal Django
    # views is the easiest way to accomplish that.
    html = everything.view(request).content.decode('utf-8')

    return render(request, 'home.html', {
        'rendered_example': SafeString(html),
        'template_source': render_template_source('everything.html'),
        'python_source': render_python_source('everything.py'),
    })
