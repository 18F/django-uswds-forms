Introduction
============

The `U.S. Web Design Standards <https://standards.usa.gov/>`_ are awesome, but there's a
few barriers that make it difficult to use with 
:class:`django.forms.Form`. For example:

* Individual checkboxes and radio buttons have different HTML
  markup than that rendered by Django forms.

* Dates are split up into three separate month/day/year
  fields.

* Dates and sets of checkboxes and radios need to use either
  ``<legend>`` or `ARIA group roles <https://www.deque.com/blog/aria-group-viable-alternative-fieldset-legend/>`_ to be accessible.

We implemented solutions for the above issues in
`CALC <https://github.com/18F/calc>`_ but wanted to factor them out for
reuse by other Django projects, so we created this package.
