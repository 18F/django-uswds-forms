import os
from setuptools import setup, find_packages

MY_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    '''
    Get the version number. It's in our package's __init__.py, but
    we don't want to import it directly b/c this will bring in
    a bunch of other dependencies that might not be on the user's
    system, so we need to be a bit hacky here.
    '''

    for line in open(os.path.join(MY_DIR, 'uswds_forms', '__init__.py')):
        if line.startswith('VERSION'):
            globs = {}
            exec(line, globs)
            return globs['VERSION']

    raise Exception('VERSION not found!')


setup(name='django-uswds-forms',
      zip_safe=False,
      version=get_version(),
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
