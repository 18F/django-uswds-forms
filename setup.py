from setuptools import setup, find_packages

from uswds_forms import VERSION


setup(name='django-uswds-forms',
      zip_safe=False,
      version=VERSION,
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
          'django>=1.8,<2',
      ],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Framework :: Django :: 1.8',
          'Framework :: Django :: 1.9',
          'Framework :: Django :: 1.10',
          'Framework :: Django :: 1.11',
          'Intended Audience :: Developers',
          'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'],
      )
