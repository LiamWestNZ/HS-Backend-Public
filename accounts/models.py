from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
import uuid



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, number, waiver, password=None,):
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")
        if not number:
            raise ValueError("Users must have a phone number, Mobile number preffered")
        if not waiver:
            raise ValueError("Users must agree to the policies and waivers")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            number=number,
            waiver=waiver,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password, first_name, last_name, number, waiver):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            number=number,
            waiver=waiver,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=40, unique=True)
    first_name = models.TextField(max_length=30, unique=False)
    last_name = models.TextField(max_length=30, unique=False)
    username = models.CharField(max_length=30, unique=False)
    number = models.CharField(max_length=20, verbose_name='Phone Number', null=False, blank=False, unique=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    waiver = models.BooleanField(verbose_name='I agree', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','number', 'waiver']

    objects = MyAccountManager()

    class Meta:
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.first_name + " " + "(" + self.username + ")"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.first_name + instance.last_name + "#" + uuid.uuid4().hex[:5]
pre_save.connect(set_username, sender=Accounts)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    
