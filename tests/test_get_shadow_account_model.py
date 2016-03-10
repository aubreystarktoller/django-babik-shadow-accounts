from django.test import TestCase, override_settings
from django.core.exceptions import ImproperlyConfigured
from babik_shadow_accounts import get_shadow_account_model
from babik_shadow_accounts.models import ShadowAccount
from tests.testapp.models import CustomShadowAccount


class GetShadowAccountModelTestCase(TestCase):
    def test_get_shadow_account(self):
        self.assertEqual(get_shadow_account_model(), ShadowAccount)

    @override_settings(
        BABIK_SHADOW_ACCOUNT_MODEL='testapp.CustomShadowAccount'
    )
    def test_swappable_shadow_account(self):
        self.assertEqual(get_shadow_account_model(), CustomShadowAccount)

    @override_settings(
        BABIK_SHADOW_ACCOUNT_MODEL='badsetting'
    )
    def test_swappable_shadow_account_bad_setting(self):
        with self.assertRaises(ImproperlyConfigured):
            get_shadow_account_model()

    @override_settings(
        BABIK_SHADOW_ACCOUNT_MODEL='thismodel.doesnotexist'
    )
    def test_swappable_shadow_account_nonexistant_model(self):
        with self.assertRaises(ImproperlyConfigured):
            get_shadow_account_model()
