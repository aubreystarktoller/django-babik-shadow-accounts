from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from babik_shadow_accounts import get_shadow_account_model


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_created(sender, instance, created, raw, using, update_fields,
                 **kwargs):
    """
    When a user is created this searches for an Account object
    and adds the user to the account if an account is found
    """
    if created:
        AccountModel = get_shadow_account_model()

        fields = getattr(settings, 'BABIK_SHADOW_ACCOUNT_GLUE_FIELDS', None)
        if not fields:
            fields = {'email': 'email'}
        kwargs = {f1: getattr(instance, f2) for f1, f2 in fields.items()}

        try:
            account = AccountModel.objects.get(**kwargs)
            account.user = instance
            account.save()
        except AccountModel.DoesNotExist:
            kwargs['user'] = instance
            account = AccountModel.objects.create(**kwargs)
