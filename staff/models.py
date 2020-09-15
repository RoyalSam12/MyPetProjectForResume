from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    post = models.CharField(max_length=40)
    salary = models.PositiveIntegerField(default=0, blank=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Detail(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    detail_text = models.CharField(max_length=300, null=True)
    e_mail = models.EmailField(null=True)
    address = models.CharField(max_length=150, null=True)


