from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Person(models.Model):

    education = [
        ("PHD", "doctora"),
        ("MST", "arshad")
    ]

    first_name = models.CharField(max_length=100, verbose_name="First Name", db_column="first_name_db_column")
    education = models.CharField(choices=education, max_length=100, verbose_name="Education")

    class Meta:
        ordering = ['first_name']

class Company(models.Model):
    employee = models.ManyToManyField(Person, through="PersonInfo")

class PersonInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    share = models.IntegerField(default=0)