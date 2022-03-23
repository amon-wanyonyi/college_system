from msilib.schema import SelfReg
from typing_extensions import Self
from unicodedata import name
from django.db import models
from pendulum import duration
from tables import Description

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=200,null=True)
    duration=models.IntegerField(default=3,null=True,blank=True)
    fees=models.IntegerField(null=True,blank=True)
    Description=models.CharField(null=True,blank=True,max_length=10000)
    def _str_(Self):
        return str(SelfReg.name)