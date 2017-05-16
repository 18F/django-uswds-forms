Developing django-uswds-forms
=============================

.. important::

    This section is about developing django-uswds-forms
    itself, not using it in your Django project. For
    details on the latter, see the :doc:`quickstart`.

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

Running the example gallery app
-------------------------------

An example Django project provides a integration with
django-uswds-forms by presenting a variety of examples alongside their
source code. It can be used to manually ensure that everything
works as expected.

To use it, run the following from the root of the repository::

    cd example
    python manage.py migrate
    python manage.py runserver

At this point you should be able to visit the locally-hosted project.

Enabling Jinja2 mode
~~~~~~~~~~~~~~~~~~~~

By default, the example gallery app renders all its examples using
their Django template source. However, the examples also need to
work on Jinja2! To make sure that they do, you'll want to run the
app in Jinja2 mode, which can be done by setting the following
environment variable prior to running the app::

    export TEMPLATE_ENGINE=jinja2

Running tests
-------------

You can run all the tests with code coverage::

    pytest

You can also ensure that there aren't any linting errors::

    flake8

To run all tests, linters, and other automated QA against
all supported runtimes and dependencies, run::

    tox

Writing documentation
---------------------

If you want to work on documentation, you can run the development
documentation server with::

    python setup.py devdocs
