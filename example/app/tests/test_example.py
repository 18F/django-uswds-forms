from django.test import TestCase, override_settings

from ..example import add_links_to_docs


@override_settings(DOCS_URL="http://docs/")
class AddLinksToDocsTests(TestCase):
    def test_it_does_nothing_when_docs_have_no_links(self):
        self.assertEqual(add_links_to_docs('foo bar baz'), 'foo bar baz')

    def test_it_hyperlinks_uswds_links(self):
        self.assertEqual(
            add_links_to_docs('foo uswds_forms.UswdsForm baz'),
            'foo <a href="http://docs/reference.html#uswds_forms.UswdsForm">'
            '<code>UswdsForm</code></a> baz'
        )

    def test_it_does_not_hyperlink_final_periods(self):
        self.assertEqual(
            add_links_to_docs('foo uswds_forms.UswdsForm. yup.'),
            'foo <a href="http://docs/reference.html#uswds_forms.UswdsForm">'
            '<code>UswdsForm</code></a>. yup.'
        )
