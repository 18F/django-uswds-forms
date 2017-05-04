import django

USE_NEW_FORM_API = django.VERSION[0] >= 1 and django.VERSION[1] >= 11
