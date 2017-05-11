from django.test import SimpleTestCase
from django import forms

from uswds_forms import UswdsCheckboxSelectMultiple, UswdsRadioSelect


def test_checkbox_select_multiple_uses_unstyled_list():
    class MyForm(forms.Form):
        checkboxes = forms.MultipleChoiceField(
            widget=UswdsCheckboxSelectMultiple,
            choices=(('one', 'One'), ('two', 'Two')),
        )

    # Note that this will fail if Django < 1.11.1!
    assert 'usa-unstyled-list' in MyForm().as_p()


def test_radio_select_uses_unstyled_list():
    class MyForm(forms.Form):
        radios = forms.ChoiceField(
            widget=UswdsRadioSelect,
            choices=(('one', 'One'), ('two', 'Two')),
        )

    # Note that this will fail if Django < 1.11.1!
    assert 'usa-unstyled-list' in MyForm().as_p()


class CheckboxTests(SimpleTestCase):
    def test_it_raises_error_when_id_is_not_present(self):
        chk = UswdsCheckboxSelectMultiple(choices=[('1', 'foo')])
        with self.assertRaisesRegexp(
            ValueError,
            'USWDS-style inputs must have "id" attributes'
        ):
            chk.render('my-checkboxes', '1')

    def test_it_renders(self):
        chk = UswdsCheckboxSelectMultiple(
            {'id': 'baz'},
            choices=[('1', 'foo'), ('2', 'bar')]
        )
        print(chk.render('my-checkboxes', '1'))
        self.assertHTMLEqual(
            chk.render('my-checkboxes', '1'),
            ('<ul id="baz" class="usa-unstyled-list">'
             '  <li>'
             '    <input checked="checked" id="baz_0" name="my-checkboxes" '
             '     type="checkbox" value="1" />'
             '    <label for="baz_0">foo</label>'
             '  </li>'
             '  <li>'
             '    <input id="baz_1" name="my-checkboxes" type="checkbox" '
             '     value="2" />'
             '    <label for="baz_1">bar</label>'
             '  </li>'
             '</ul>')
        )


class RadioTests(SimpleTestCase):
    def test_it_raises_error_when_id_is_not_present(self):
        rad = UswdsRadioSelect(choices=[('1', 'foo')])
        with self.assertRaisesRegexp(
            ValueError,
            'USWDS-style inputs must have "id" attributes'
        ):
            rad.render('my-radios', '1')

    def test_it_renders(self):
        rad = UswdsRadioSelect(
            {'id': 'baz'},
            choices=[('1', 'foo'), ('2', 'bar')]
        )
        self.assertHTMLEqual(
            rad.render('my-radios', '1'),
            ('<ul id="baz" class="usa-unstyled-list">'
             '  <li>'
             '    <input checked="checked" id="baz_0" name="my-radios" '
             '     type="radio" value="1" />'
             '    <label for="baz_0">foo</label>'
             '  </li>'
             '  <li>'
             '    <input id="baz_1" name="my-radios" type="radio" '
             '     value="2" />'
             '    <label for="baz_1">bar</label>'
             '  </li>'
             '</ul>')
        )
