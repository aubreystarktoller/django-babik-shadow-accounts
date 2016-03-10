from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from babik_shadow_accounts import get_shadow_account_model

class BabikAccountsTestCase(TestCase):
    def test_account_created_on_user_save(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            email='test@example.net',
            glue_field='test',
            password='top_secret'
        )

        AccountModel = get_shadow_account_model()
        accounts = list(AccountModel.objects.all())

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].user, user)

    def test_account_updated_on_user_save(self):
        AccountModel = get_shadow_account_model()
        account = AccountModel.objects.create(email='test@example.net')

        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            email='test@example.net',
            glue_field='test',
            password='top_secret'
        )

        account = AccountModel.objects.get(pk = account.pk)

        self.assertEqual(account.user, user)

    def test_already_saved(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            email='test@example.net',
            glue_field='test',
            password='top_secret'
        )
        user.save()

        AccountModel = get_shadow_account_model()
        accounts = list(AccountModel.objects.all())

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].user, user)

    @override_settings(
        BABIK_SHADOW_ACCOUNT_GLUE_FIELDS = {'slug': 'glue_field'},
        BABIK_SHADOW_ACCOUNT_MODEL = 'testapp.CustomShadowAccount',
    )
    def test_custom_glue_fields(self):
        AccountModel = get_shadow_account_model()
        account = AccountModel.objects.create(slug='test')

        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            email='test@example.net',
            glue_field='test',
            password='top_secret'
        )

        account = AccountModel.objects.get(pk=account.pk)

        self.assertEqual(account.user, user)
