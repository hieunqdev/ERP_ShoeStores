from email.policy import default
from django.db import models

# Create your models here.


class WorkTime(models.Model):
    name = models.CharField(max_length=150)
    day = models.CharField(max_length=150)
    start_time = models.CharField(max_length=150)
    end_time = models.CharField(max_length=150)
    start_day = models.CharField(max_length=150, null=True, blank=True)
    end_day = models.CharField(max_length=150, null=True, blank=True)
    time = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER_CHOICES = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
    )
    cover_image = models.ImageField(
        null=True, blank=True, upload_to="covers/%Y/%m/%D")
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="Nam")
    email = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)
    work_time = models.ForeignKey(
        WorkTime, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
