from django.db import models


# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=255)
    msisdn = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Clogs(models.Model):
    customer = models.ForiegnKey(Customers, on_delete=models.CASCADE)
    imsi = models.CharField(max_legth=10)
    imei = models.CharField(max_legth=10)
    plan = models.CharField(max_legth=10)
    call_type = models.CharField(max_legth=10)
    corresp_type = models.CharField(max_legth=10)
    corresp_isdn = models.CharField(max_legth=10)
    duration = models.IntegerField(max_legth=10)
    time = models.TimeField(max_legth=10)
    date = models.DateField(max_legth=10)

    def __str__(self):
        return f"{self.customer.name}-{self.date}-{self.call_type}"
