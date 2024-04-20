from typing import Any
from django.db import models

from django.utils.translation import gettext_lazy as _
from commons.models import AbstractCommonModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, **kwargs: Any) -> Any:
        user = self.model(**kwargs)
        user.set_password(kwargs.get("password"))
        user.save(using=self._db)
        return user

    def create_user(self, **kwargs: Any) -> Any:
        kwargs["is_admin"] = False
        return self._create_user(**kwargs)

    def create_superuser(self, **kwargs: Any) -> Any:
        kwargs["is_admin"] = True
        return self._create_user(**kwargs)


class User(AbstractCommonModel, AbstractBaseUser):

    email = models.CharField(
        _("Email"), unique=True, max_length=120, db_index=True, null=False, blank=False
    )
    password = models.CharField(_("Password"), max_length=128, null=False, blank=False)
    username = models.CharField(_("Username"), unique=True, max_length=120)
    is_active = models.BooleanField(
        _("Active"), default=True, help_text="Designates Whether A User Is Active"
    )
    is_admin = models.BooleanField(
        _("Admin"), default=False, help_text="Designates Whether A User Is An Admin"
    )
    USERNAME_FIELD = "username"
    objects = UserManager()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_active and self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def get_all_permissions(self,  obj=None):
        return []

    class Meta(AbstractCommonModel.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")
