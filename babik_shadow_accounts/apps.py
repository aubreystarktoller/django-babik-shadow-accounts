from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BabikShadowAccountsConfig(AppConfig):
    name = 'babik_shadow_accounts'
    verbose_name = _('Babik Shadow Accounts')

    def ready(self):
        import babik_shadow_accounts.signals.handlers
