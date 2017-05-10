import os
from setuptools import setup, find_packages
import distutils.cmd
import subprocess

import metadata


class SimpleCommand(distutils.cmd.Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class DevDocsCommand(SimpleCommand):
    description = "Run development server for documentation"

    def run(self):
        subprocess.check_call(
            ['sphinx-autobuild', '.', '_build/html', '-p', '8001',
             '-z', os.path.join('..', 'uswds_forms')],
            cwd='docs'
        )


setup(name='django-uswds-forms',
      cmdclass={
          'devdocs': DevDocsCommand,
      },
      zip_safe=False,
      version=metadata.get_version(),
      description='Django Forms integration with the U.S. Web Design Standards',

      # TODO: Add long_description.

      author='Atul Varma',
      author_email='atul.varma@gsa.gov',
      license='Public Domain',
      url='https://github.com/18F/django-uswds-forms',
      package_dir={'uswds_forms': 'uswds_forms'},
      include_package_data=True,
      packages=find_packages(),
      install_requires=[
          'django>=1.11.1,<2',
      ],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.11',
          'Intended Audience :: Developers',
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'],
      )
