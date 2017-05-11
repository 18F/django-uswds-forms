=============
API reference
=============

Template tags
=============

.. highlight:: html+django

To use the following template tags, you'll need to load this package's
custom template tag set in your templates like so::

    {% load uswds_forms %}

.. _fieldset-template-tag:

``fieldset``
------------

The ``{% fieldset %}`` tag can be used to render a form field using
the ``<fieldset>`` element. The field's label is also rendered,
along with any associated form errors and help text.

Markup is also added to ensure that screen reader users will have an
easy time navigating grouped lists of options.

Sample usage::

    {% fieldset my_form.name %}
    {% fieldset my_form.address %}
    {% fieldset my_form.birthday %}

.. highlight:: python

.. currentmodule:: uswds_forms

Form
====

.. autoclass:: UswdsForm()
   :members: as_fieldsets

.. _formfields:

Form fields
===========

These fields use the same :ref:`core field arguments
<django:core-field-arguments>` as core Django.

.. autoclass:: UswdsDateField(**kwargs)

.. autoclass:: UswdsMultipleChoiceField(**kwargs)

.. _widgets:

Widgets
=======

.. autoclass:: UswdsCheckboxSelectMultiple()

.. autoclass:: UswdsDateWidget()
   :members: template_name, get_context

.. autoclass:: UswdsRadioSelect()

Other utilities
===============

.. autoclass:: UswdsErrorList()
