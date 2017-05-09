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

* Your project needs to use Python 3.

Required settings
~~~~~~~~~~~~~~~~~

Add ``uswds_forms`` to your ``INSTALLED_APPS`` setting, e.g.:

.. code-block:: python

   INSTALLED_APPS = (
       # ...
       'uswds_forms',
       # ...
   )
