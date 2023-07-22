from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password


# Create your models here.

class CustomUserManager (UserManager):
    def _create_user(self, username,  password, **extra_fields):
        # if not email:
        #     raise ValueError("You have not provided a valid e-mail address")
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        hashed = make_password(password)
        print(hashed)
        user.set_password(hashed)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username=None,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255, blank=True, default='', unique=True)
    # email = models.EmailField(blank=True, default='')

    name = models.CharField(
        max_length=70, blank=True, default='')
    field_choices = [
        ("Author", "Author"),
        ("Reader", "Reader")
    ]

    role = models.CharField(
        choices=field_choices,
        max_length=6,
        default="Reader",
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Book(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    title = models.CharField(max_length=255, blank=False, unique=True)
    authorName = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, blank=False, null=False)
    text = models.TextField(null=False)
