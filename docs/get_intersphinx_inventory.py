'''
    This command-line program makes it easy to get the Sphinx
    inventory file for a third-party project, and catalog it.

    Run this script without any arguments for help.
'''

import sys
import subprocess

import conf


if __name__ == '__main__':
    mapping = conf.intersphinx_mapping
    if len(sys.argv) < 2 or sys.argv[1] not in mapping:
        print("Usage: {} [{}]".format(
            sys.argv[0],
            '|'.join(mapping.keys()),
        ))
        sys.exit(1)

    uri, obj_uri = mapping[sys.argv[1]]
    if obj_uri is None:
        obj_uri = uri + '/objects.inv'

    # http://stackoverflow.com/a/36831198
    subprocess.check_call([
        sys.executable, '-m', 'sphinx.ext.intersphinx',
        obj_uri,
    ])
