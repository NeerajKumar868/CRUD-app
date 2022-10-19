from django.db import models


# Create your models here.

class Employee(models.Model):
    EmpID=models.IntegerField()
    EmpName=models.TextField(max_length=50)
    EmpSalary=models.FloatField(max_length=15)
    EmpTeam=models.TextField(default='Mumbai')
