from django.utils.safestring import SafeString
from django.utils.module_loading import import_string
from django.urls import reverse

from .render_source import render_template_source, render_python_source

class Example:
    def __init__(self, basename):
        self.basename = basename
        self.view = import_string('app.examples.' + basename + '.view')

        docstr = import_string('app.examples.' + basename + '.__doc__')
        self.name, self.description = docstr.split('\n\n', 1)
        self.python_source = render_python_source(basename + '.py')

    @property
    def template_source(self):
        return render_template_source(self.basename + '.html')

    @property
    def url(self):
        return reverse('example', args=(self.basename,))

    def render(self, request):
        # This is sort of weird because we're decoding the
        # content in a HttpResponse; it's not an ideal API,
        # but we want the examples be as conventional as
        # possible so they don't confuse readers, and having
        # them return HttpResponse objects like normal Django
        # views is the easiest way to accomplish that.
        return SafeString(self.view(request).content.decode('utf-8'))
