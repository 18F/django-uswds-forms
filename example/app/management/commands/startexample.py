import re
from pathlib import Path
from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError

from app.example import Example, APP_DIR

SLUG_RE = re.compile('^[A-Za-z0-9_]+$')
SLUG_HELP = "Alphanumerics and underscores only"
EXAMPLE_NAMES_PATH = "app.views.EXAMPLE_NAMES"
EXAMPLE_TESTS_PATH = APP_DIR / 'tests' / 'test_examples.py'
TEMPLATE_NAME = '_startexample_template'


def untemplatize(f: Path, example: Example):
    return f.read_text().replace(TEMPLATE_NAME, example.basename)


class Command(BaseCommand):
    help = 'Creates a new example for the gallery.'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument(
            'example_slug',
            help="Slug for example. {}.".format(SLUG_HELP)
        )
        parser.add_argument(
            '--undo',
            action='store_true',
            help='Undo an earlier invocation of this command.'
        )

    def undo_copy(self, src: Path, dest: Path, example: Example) -> None:
        relpath = dest.relative_to(Path.cwd())
        if not dest.exists():
            self.stdout.write("Hmm, {} does not exist.".format(relpath))
        elif dest.read_text() != untemplatize(src, example):
            self.stdout.write("{} has changed, not deleting.".format(relpath))
        else:
            dest.unlink()
            self.stdout.write("Deleted {}.".format(relpath))

    def copy(self, src: Path, dest: Path, example: Example) -> None:
        relpath = dest.relative_to(Path.cwd())
        if dest.exists():
            self.stdout.write("{} exists, not overwriting.".format(relpath))
        else:
            dest.write_text(untemplatize(src, example))
            self.stdout.write("Created {}.".format(relpath))

    def handle(self, example_slug: str, undo: bool, **kwargs):
        if not SLUG_RE.match(example_slug):
            raise CommandError('Invalid slug! {}.'.format(SLUG_HELP))

        template = Example(TEMPLATE_NAME)
        ex = Example(example_slug)

        if undo:
            self.undo_copy(template.template_path, ex.template_path, ex)
            self.undo_copy(template.jinja2_path, ex.jinja2_path, ex)
            self.undo_copy(template.python_path, ex.python_path, ex)
        else:
            self.copy(template.template_path, ex.template_path, ex)
            self.copy(template.jinja2_path, ex.jinja2_path, ex)
            self.copy(template.python_path, ex.python_path, ex)

            self.stdout.write("\nDone! Now edit the above files.")
            self.stdout.write("Then, add '{}' to {}.".format(
                example_slug,
                EXAMPLE_NAMES_PATH,
            ))
            self.stdout.write(
                "You may also want to write tests for "
                "the example in {}.".format(
                    EXAMPLE_TESTS_PATH.relative_to(Path.cwd())
                )
            )
