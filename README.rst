============================
Django Babik Shadow Accounts
============================

.. image:: https://img.shields.io/badge/license-BSD-red.svg
   :targer: https://raw.githubusercontent.com/aubreystarktoller/django-babik-shadow-accounts/master/LICENSE

.. image:: https://travis-ci.org/aubreystarktoller/django-babik-shadow-accounts.svg?branch=master
   :target: https://travis-ci.org/aubreystarktoller/django-babik-shadow-accounts

.. image:: https://coveralls.io/repos/github/aubreystarktoller/django-babik-shadow-accounts/badge.svg?branch=master
   :target: https://coveralls.io/github/aubreystarktoller/django-babik-shadow-accounts?branch=master 

A tiny Django app that adds "shadow accounts" - accounts that represent users
but are not necessarily linked to user accounts.

This app also will automatically link a user account to its corresponding
shadow account when the user account is created, or create a shadow account
if one does not exist. To do this it is assumed that the shadow account and
the user account have some fields in common which also distinguish them. The
default is to assume both the shadow account and the user account have a
not-empty e-mail field. The default can be changed using the
``BABIK_SHADOW_ACCOUNT_GLUE_FIELDS`` setting (see SETTINGS for more
information).

An example usage would be an e-commerce site where users where not required
to login to make a purchase. Instead of linking orders to a user account
orders would be linked to a shadow account. A user's orders would be
attached to a single record without a user account having to be created, and
the user would be able to create an account in the future and view past orders
without any confusion.

Lastly this package includes a very bare bones model for the shadow account
and it is assumed that it is desirable to extend this model to include more
fields and as such this has been made a swappable model - just set
``BABIK_SHADOW_ACCOUNT_MODEL`` to the model you wish to use to represent a
shadow account (see SETTINGS for more information).

INSTALLATION
============

Django Versions Supported:

* Django 1.8 with Python 2.7, 3.2, 3.3 and 3.4
* Django 1.9 with Python 2.7, 3.4 and 3.5

To install using pip:

::

    pip install git+https://github.com/aubreystarktoller/django-babik-shadow-accounts.git

You can obtain the source for ``django-babik-accounts`` from:

::

    https://github.com/aubreystarktoller/django-babik-accounts

SETTINGS
========

BABIK_SHADOW_ACCOUNT_MODEL
-------------------
Default: ``"babik_shadow_accounts.Account"``

The model to use to represent an account. This must provide a one-to-one
relation to ``AUTH_USER_MODEL`` and this relation must be able to be ``NULL``.

BABIK_SHADOW_ACCOUNT_GLUE_FIELDS
-------------------------
Default: ``{"email": "email"}``

The fields that user accounts and shadow accounts have in common. Must be a
dictionary whose keys are fields on the shadow account model and whose
values must be fields on the user model. When a user is created this setting
acts as a mapping between a shadow account model's fields and a user model's
fields allowing a shadow account to be found if one exists.

MODELS
======

``babik_shadow_account.models.BaseShadowAccount``

A basis for a shadow account model including an e-mail field and a one-to-one
relation to the user model. It is not nessary to use this when creating a 
custom a custom shadow account model.

``babik_shadow_account.models.ShadowAccount``

A simple shadow account model which just inherits from ``BaseShadowAccount``.
This swappable using the ``BABIK_SHADOW_ACCOUNT_MODEL`` setting.

UTILITIES
========

``babik_shadow_account.get_shadow_account_models()`` returns the current
shadow account model

TESTING
=======

To run the tests first clone the git repo:

    git clone https://github.com/aubreystarktoller/django-babik-account
    cd django-babkik-account
  
To run the tests you'll require ``make``. It is recommended that use tox to run
the tests:
    
    tox

To run the tests in the current environment:

    make test


AUTHORS
=======
Aubrey Stark-Toller

LICENSE
=======
``django-babik-shadow-accounts`` is licensed under the BSD license. See
LICENSE for the full license.
