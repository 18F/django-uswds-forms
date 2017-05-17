from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.utils.six import StringIO
from django.utils.module_loading import import_string

from app.example import Example
from app.management.commands.startexample import (
    EXAMPLE_NAMES_PATH,
    EXAMPLE_TESTS_PATH,
)


class ClosepollTest(TestCase):
    def setUp(self):
        self.example = Example('zzz')
        self.paths = [
            self.example.template_path,
            self.example.jinja2_path,
            self.example.python_path
        ]
        self.cleanup_paths()

    def tearDown(self):
        self.cleanup_paths()

    def cleanup_paths(self):
        for path in self.paths:
            if path.exists():
                path.unlink()

    def call(self, *args):
        out = StringIO()
        call_command('startexample', *args, stdout=out)
        return out.getvalue()

    def test_example_names_path_exists(self):
        import_string(EXAMPLE_NAMES_PATH)

    def test_example_tests_path_exists(self):
        self.assertTrue(EXAMPLE_TESTS_PATH.exists())

    def test_undo_does_not_delete_modified_files(self):
        self.call(self.example.basename)
        for path in self.paths:
            path.write_text("i am changed!")
        output = self.call(self.example.basename, '--undo')
        self.assertIn('has changed, not deleting', output)

    def test_undo_does_not_explode_if_files_do_not_exist(self):
        output = self.call(self.example.basename, '--undo')
        self.assertIn('does not exist', output)

    def test_create_does_not_overwrite(self):
        self.call(self.example.basename)
        output = self.call(self.example.basename)
        self.assertIn('not overwriting', output)

    def test_create_works(self):
        output = self.call(self.example.basename)
        self.assertIn('Created', output)
        for path in self.paths:
            self.assertTrue(path.exists(), '{} was created'.format(path))
        self.assertIn(self.example.basename,
                      self.example.python_path.read_text())

    def test_undo_works(self):
        self.call(self.example.basename)
        output = self.call(self.example.basename, '--undo')
        self.assertIn('Deleted', output)
        for path in self.paths:
            self.assertFalse(path.exists(), '{} was removed'.format(path))

    def test_invalid_slug_raises_error(self):
        with self.assertRaisesRegex(CommandError, 'Invalid slug'):
            self.call('boop?!')
