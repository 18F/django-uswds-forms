[![Build Status](https://travis-ci.org/18F/django-uswds-forms.svg?branch=master)](https://travis-ci.org/18F/django-uswds-forms)

This is a work-in-progress and may eventually be subsumed into
[django-designstandards][] depending on what's best for everyone.

## Motivation

The [U.S. Web Design Standards][uswds] are awesome, but there's a
few barriers that make it difficult to use with the
[Django `Form` class][django-forms]:

* Individual checkboxes and radio buttons have different HTML
  markup than that rendered by Django forms.

* Dates are split up into three separate month/day/year
  fields.

* Dates and sets of checkboxes and radios need to use either
  `<legend>` or [ARIA group roles][] to be accessible.

We implemented solutions for the above issues in [CALC][] but
wanted to factor them out for reuse by other Django projects, so
we created this package.

## Prerequisites

* This package contains *no static files*.  This means you need
  to bring in USWDS from somewhere else--use whatever your
  preferred method from the [USWDS developer guide][].

  You *should* be able to use any version of USWDS you want, as
  this package only really depends on the HTML structure and CSS
  classes of a handful of USWDS widgets.

  You'll also need to make sure the USWDS CSS is included in
  whatever pages you want to display your forms on.

* You'll need Django 1.11.1 or later.

* Your project needs to use Python 3.

## Quick start

We still need to add proper documentation on how to *use* the package.

For now, to develop on the package itself, you can run:

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

At this point you may want to use `pip` to install a specific version
of Django in your virtualenv. If you don't, that's fine--the next
step will just install the latest version of Django that this
package supports.

Now install the package in development mode:

```
python setup.py develop
```

You can then run the example app:

```
cd example
python manage.py runserver
```

Or, to work on the documentation, run:

```
python setup.py devdocs
```

[django-designstandards]: https://github.com/department-of-veterans-affairs/django-designstandards
[uswds]: https://standards.usa.gov/
[django-forms]: https://docs.djangoproject.com/en/1.11/topics/forms/#the-django-form-class
[ARIA group roles]: https://www.deque.com/blog/aria-group-viable-alternative-fieldset-legend/
[CALC]: https://github.com/18F/calc
[USWDS developer guide]: https://standards.usa.gov/getting-started/developers/
