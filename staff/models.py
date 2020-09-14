from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    post = models.CharField(max_length=40)
    salary = models.PositiveIntegerField(default=0, blank=False)


class Detail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    detail_text = models.CharField(max_length=300)
    e_mail = models.EmailField()
    address = models.CharField(max_length=150)
