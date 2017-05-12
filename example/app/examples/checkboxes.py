'''
Multiple checkboxes

This example shows how to render groups of checkboxes using
a uswds_forms.UswdsMultipleChoiceField.
'''

from django.shortcuts import render
import uswds_forms


class MyForm(uswds_forms.UswdsForm):
    states = uswds_forms.UswdsMultipleChoiceField(
        label="What states have you visited?",
        required=False,
        choices=(
            ('OH', 'Ohio'),
            ('IL', 'Illinois'),
            ('CA', 'California'),
        )
    )


def view(request):
    return render(request, 'examples/checkboxes.html', {
        'form': MyForm() if request.method == 'GET' else MyForm(request.POST)
    })
