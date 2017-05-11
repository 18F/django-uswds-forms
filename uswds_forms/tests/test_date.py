from datetime import date
from django.test import SimpleTestCase
from django.core.exceptions import ValidationError

from uswds_forms.date import UswdsDateWidget, UswdsDateField


class DateWidgetTests(SimpleTestCase):
    def test_render_assigns_ids_and_labels(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', None, {'id': 'blarg'})
        self.assertRegexpMatches(content, 'id="blarg_0"')
        self.assertRegexpMatches(content, 'id="blarg_1"')
        self.assertRegexpMatches(content, 'id="blarg_2"')
        self.assertRegexpMatches(content, 'for="blarg_0"')
        self.assertRegexpMatches(content, 'for="blarg_1"')
        self.assertRegexpMatches(content, 'for="blarg_2"')

    def test_render_assigns_names(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', None, {'id': 'blarg'})
        self.assertRegexpMatches(content, 'name="boop_0"')
        self.assertRegexpMatches(content, 'name="boop_1"')
        self.assertRegexpMatches(content, 'name="boop_2"')

    def test_render_assigns_hint_id_and_aria_describedby(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', None, {'id': 'foo'})
        self.assertRegexpMatches(content, 'id="foo_hint"')
        self.assertRegexpMatches(content, 'aria-describedby="foo_hint"')

    def test_render_takes_value_as_list(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', [2006, 7, 29], {'id': 'foo'})
        self.assertRegexpMatches(content, 'value="2006"')
        self.assertRegexpMatches(content, 'value="7"')
        self.assertRegexpMatches(content, 'value="29"')

    def test_render_takes_value_as_date(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', date(2005, 6, 28), {'id': 'foo'})
        self.assertRegexpMatches(content, 'value="2005"')
        self.assertRegexpMatches(content, 'value="6"')
        self.assertRegexpMatches(content, 'value="28"')

    def test_render_does_not_raise_exception_on_empty_lists(self):
        widget = UswdsDateWidget()
        content = widget.render('boop', [], {'id': 'foo'})

        # The <input>s should not have any 'value' attribute whatsoever.
        self.assertNotRegexpMatches(content, 'value')

    def test_decompress_works_with_dates(self):
        widget = UswdsDateWidget()
        self.assertEqual(widget.decompress(date(2005, 6, 28)), [2005, 6, 28])

    def test_decompress_works_with_none(self):
        widget = UswdsDateWidget()
        self.assertEqual(widget.decompress(None), [None, None, None])


class DateFieldTests(SimpleTestCase):
    def test_compress_returns_date_for_valid_dates(self):
        field = UswdsDateField()
        self.assertEqual(field.compress([2005, 6, 28]), date(2005, 6, 28))

    def test_compress_raises_validation_errors_for_invalid_dates(self):
        field = UswdsDateField()

        with self.assertRaisesRegexp(
            ValidationError,
            'Invalid date: day is out of range for month.'
        ):
            field.compress([2001, 2, 31])

    def test_compress_returns_none_when_data_list_is_falsy(self):
        field = UswdsDateField()
        self.assertEqual(field.compress(None), None)
        self.assertEqual(field.compress([]), None)
