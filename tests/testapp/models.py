from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from babik_shadow_accounts.models import BaseShadowAccount


class CustomShadowAccount(BaseShadowAccount):
    slug = models.SlugField()


class CustomUserManager(BaseUserManager):
    def create_user(self, email, glue_field, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            glue_field=glue_field
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    glue_field = models.SlugField()

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def get_group_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
