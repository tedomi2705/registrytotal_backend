from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Inspection(models.Model):
    inspection_id = models.IntegerField(primary_key=True)
    certificate_no = models.CharField(max_length=20, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    inspected_by = models.CharField(max_length=50, blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.CASCADE)


class InspectionCenter(models.Model):
    center_id = models.IntegerField(primary_key=True)
    center_name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)


class InspectionRecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    result = models.CharField(max_length=50)
    center_id = models.ForeignKey('InspectionCenter', on_delete=models.CASCADE)
    inspection_id = models.ForeignKey('Inspection', on_delete=models.CASCADE)


class Owner(models.Model):
    owner_id = models.IntegerField(primary_key=True)
    owner_info = models.CharField(max_length=50)
    owner_type = models.CharField(max_length=20)
    province = models.CharField(max_length=50)


class Upload(models.Model):
    upload_id = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=50)
    file_size = models.IntegerField(blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    center_id = models.ForeignKey('InspectionCenter', on_delete=models.CASCADE)



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(primary_key=True)
    manufacturer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    plate_no = models.CharField(max_length=20)
    province = models.CharField(max_length=50)
    registration_cert_no = models.CharField(max_length=20)
    registration_date = models.DateField(blank=True, null=True)
    usage_purpose = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    owner_id = models.ForeignKey('Owner', on_delete=models.CASCADE)
