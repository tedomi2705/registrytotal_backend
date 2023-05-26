from django.db import models


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


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length=20)
    username = models.CharField(max_length=50)


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
