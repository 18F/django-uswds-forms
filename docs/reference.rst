=============
API reference
=============

.. _template-tags:

Template tags
=============

.. highlight:: html+django

.. important::

    This section is for projects using Django's default
    :class:`~django.template.backends.django.DjangoTemplates` backend. For
    projects using Jinja2, see the :ref:`jinja2-functions` section.

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

.. _jinja2-functions:

Jinja2 functions
================

.. important::

    This section is for projects using Django's
    :class:`~django.template.backends.jinja2.Jinja2` backend. For
    projects using Django templates, see the :ref:`template-tags` section.

For details on how to register any of these functions with your Jinja2
environment, see :ref:`jinja2-setup`.

.. autofunction:: fieldset

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

All of the following widgets work with
the :class:`~django.forms.renderers.DjangoTemplates` and
:class:`~django.forms.renderers.Jinja2` form renderers.

.. autoclass:: UswdsCheckboxSelectMultiple()

.. autoclass:: UswdsDateWidget()
   :members: template_name, get_context

.. autoclass:: UswdsRadioSelect()

Other utilities
===============

.. autoclass:: UswdsErrorList()
