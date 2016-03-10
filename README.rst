============================
Django Babik Shadow Accounts
============================

A tiny Django app that adds "shadow accounts" - accounts that represent users
(as in people) but are not necessarily linked to user accounts (as in the
representation of the person in the database).

This app also will automatically link a user account to its corresponding
shadow account when the user account is created, or create a shadow account
if one does not exist. To do this it is assumed that the shadow account and
the user account have some fields in common which also distinguish them. The
default is to assume both the shadow account and the user account have an
e-mail field. The default can be changed using the
``BABIK_ACCOUNT_GLUE_FIELDS`` setting (see SETTINGS for more information).

An example usage would be an e-commerce site where users where not required
to login to make a purchase. Instead of linking orders to user accounts
orders would be linked to these shadow accounts. A user's orders would be
attached to a single record without a user account having to be created, and
the user would be able to create an account in the future and view past orders
without any confusion.

Lastly this package includes a very bare bones model for the shadow account
and it is assumed that it is desirable to extend this model to include more
fields and such this been made a swappable model - just set
``BABIK_ACCOUNT_MODEL`` to the model you wish to use to represent an account
(see SETTINGS for more information).

INSTALLATION
============

Django versions supported: 1.8, 1.9

Python versions supported: 2.7, 3.4

You can obtain the source for ``django-babik-accounts`` from:

::

    https://github.com/aubreystarktoller/django-babik-accounts

SETTINGS
========

BABIK_ACCOUNT_MODEL
-------------------
Default: 'babik_shadow_accounts.Account'

The model to use to represent an account. This must provide a one-to-one
relation to ``AUTH_USER_MODEL`` and this relation must be able to be ``NULL``.

BABIK_ACCOUNT_GLUE_FIELDS
-------------------------
Default: {'email': 'email'}

The fields that user accounts and shadow accounts have in common. Must be a
dictionary whose keys are fields on the shadow account model and whose
values must be fields on the user model. When a user is created this setting
acts as mapping between the shadow account models and the user models fields
allowing a shadow account to be found if one exists.

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
