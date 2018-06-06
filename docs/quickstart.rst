Quick start guide
=================

Prerequisites
~~~~~~~~~~~~~

* This package contains *no static files*.  This means you need
  to bring in USWDS from somewhere else--use whatever your
  preferred method from the `USWDS developer guide <https://standards.usa.gov/getting-started/developers/>`_.

  You *should* be able to use any version of USWDS you want, as
  this package only really depends on the HTML structure and CSS
  classes of a handful of USWDS widgets.

  You'll also need to make sure the USWDS CSS is included in
  whatever pages you want to display your forms on.

* You'll need Django 1.11.1 or later.

* Your project needs to use either Django's default
  :class:`~django.template.backends.django.DjangoTemplates`
  or :class:`~django.template.backends.jinja2.Jinja2`
  template engine.

  In a similar vein, your forms need to use either Django's default
  :class:`~django.forms.renderers.DjangoTemplates` or
  :class:`~django.forms.renderers.Jinja2` form renderer.

* Your project needs to use Python 3.

Installation
~~~~~~~~~~~~

.. highlight:: none

This package isn't on PyPI yet, so you'll need to install it directly
from GitHub for now::

    pip install git+git://github.com/18F/django-uswds-forms

Required settings
~~~~~~~~~~~~~~~~~

Add ``uswds_forms`` to your ``INSTALLED_APPS`` setting, e.g.:

.. code-block:: python

   INSTALLED_APPS = (
       # ...
       'uswds_forms',
       # ...
   )

.. _jinja2-setup:

Jinja2 setup (optional)
~~~~~~~~~~~~~~~~~~~~~~~

If you're using Django's default template backend, you don't need
to do any extra configuration. However, if you're using the
:class:`~django.template.backends.jinja2.Jinja2` backend,
you might want to add some of this package's :ref:`jinja2-functions` to
your Jinja2 environment.

For example, you can create ``myproject/jinja2.py`` with this content:

.. literalinclude:: ../example/app/jinja2.py
   :language: python

and in your ``settings.py``, set the ``environment`` option of the
Jinja2 template engine to point at it, like so:

.. code-block:: python

   TEMPLATES = [
       # ...
       {
           'BACKEND': 'django.template.backends.jinja2.Jinja2',
           'DIRS': [],
           'APP_DIRS': True,
           'OPTIONS': {
               'environment': 'myproject.jinja2.environment',
           }
       },
       # ...
   ]

This will allow you to use e.g. the :func:`~uswds_forms.fieldset`
function from any Jinja2 template.

Getting started
~~~~~~~~~~~~~~~

One way to get started is by visiting the example gallery.  It contains
a number of examples in increasing complexity.  Each example can be tinkered
with, and you can also easily view its Python and Django template source
code.

If you want to run the example gallery locally, see :doc:`developing`.

Guidelines
~~~~~~~~~~

These guidelines are generally followed by the aforementioned example
gallery, so refer to that if you want to see these in action.

* If possible, use the :class:`~uswds_forms.UswdsForm` class for your
  form. It will make error listings "just work", and its
  :meth:`~uswds_forms.UswdsForm.as_fieldsets` can get you by in a
  pinch; for more fine-grained display of form fields, see the
  :ref:`fieldset template tag <fieldset-template-tag>`.

* In general, Django's :ref:`built-in Field classes <built-in-fields>`
  should work okay out-of-the-box. The major exceptions to these are
  radios and checkboxes, which use slightly different markup in
  USWDS than Django's default, so you'll want to use our
  specialized :ref:`widgets <widgets>` to replace Django's defaults.

* If you want automatic indication of required fields in the style
  shown in the `USWDS name form template
  <https://standards.usa.gov/components/form-templates/#name-form>`_, 
  you can set the :attr:`~django.forms.Form.required_css_class`
  attribute on your form to ``'usa-input-required'``.

  (Unfortunately, there isn't currently an easy way to do the inverse
  of this, where only *optional* fields are called out.)
