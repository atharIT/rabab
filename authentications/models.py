from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UsersManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name,gender,type, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            gender=gender,
            type=type,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name,gender,type, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name,gender,type, password, **extra_fields)

    def create_superuser(self, email, name,gender, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name,gender,1, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    genderchoices = (('male', 'male'), ('female', 'female'))
    usertypes = ((1, "admin"), (2, "supervisor"), (3, "volunteer"))

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    gender = models.CharField(choices=genderchoices, max_length=6)
    type = models.IntegerField(choices=usertypes, default=3)
    password = models.CharField(max_length=15)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'gender','password']


class supervisor(models.Model):
    user= models.ForeignKey(Users,on_delete=models.CASCADE)
    national_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.user.email