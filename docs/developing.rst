Developing django-uswds-forms
=============================

.. highlight:: none

First, clone the git repository::

    git clone https://github.com/18F/django-uswds-forms

Then create a virtualenv for the project and install
development dependencies::

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

Then install django-uswds-forms in development mode::

    python setup.py develop

Using the example app
~~~~~~~~~~~~~~~~~~~~~

An example Django project provides a simple integration with
django-uswds-forms and can be used to manually ensure that everything
works as expected.

To use it, run the following from the root of the repository::

    cd example
    python manage.py migrate
    python manage.py runserver

At this point you should be able to visit the locally-hosted project.

Running tests
~~~~~~~~~~~~~

You can run all the tests with code coverage::

    pytest

You can also ensure that there aren't any linting errors::

    flake8

To run all tests, linters, and other automated QA against
all supported runtimes and dependencies, run::

    tox

Writing documentation
~~~~~~~~~~~~~~~~~~~~~

If you want to work on documentation, you can run the development
documentation server with::

    python setup.py devdocs
