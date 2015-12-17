from django.db import models

from datetime import date
# Create your models here.

class fir(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name + '  |  ' + str(self.timestamp.date())