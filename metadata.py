from pathlib import Path
from typing import Dict  # NOQA

MY_DIR = Path(__file__).resolve().parent

INIT_PY = MY_DIR / 'uswds_forms' / '__init__.py'


def get_version() -> str:
    '''
    Get the version number. It's in our package's __init__.py, but
    we don't want to import it directly b/c this will bring in
    a bunch of other dependencies that might not be on the user's
    system, so we need to be a bit hacky here.
    '''

    for line in open(str(INIT_PY)):
        if line.startswith('VERSION'):
            globs = {}  # type: Dict[str, str]
            exec(line, globs)
            return globs['VERSION']

    raise Exception('VERSION not found!')
