from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


default_app_config = 'babik_shadow_accounts.apps.BabikShadowAccountsConfig'


def get_shadow_account_model():
    model_name = getattr(
        settings,
        'BABIK_SHADOW_ACCOUNT_MODEL',
        'babik_shadow_accounts.ShadowAccount'
    )
    try:
        return django_apps.get_model(model_name)
    except ValueError:
        raise ImproperlyConfigured(
            "BABIK_SHADOW_ACCOUNT_MODEL must be of the form"
            " 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "BABIK_SHADOW_ACCOUNT_MODEL refers to model '%s' that has not"
            " been installed" % model_name
        )
