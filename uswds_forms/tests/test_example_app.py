'''
    This test suite runs the example app's tests.

    Ideally we would just have py.test find the tests in the
    example app and run them itself, but that would require
    ultimately calling django's configuration/setup functions
    twice from the same process, which doesn't work, so we'll just
    run the example app's test suite in a subprocess here.
'''

import sys
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

EXAMPLE_DIR = ROOT_DIR / 'example'


def test_example_app():
    subprocess.check_call([
        sys.executable, 'manage.py', 'test'
    ], cwd=str(EXAMPLE_DIR))
