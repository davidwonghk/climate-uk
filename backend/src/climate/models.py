from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Climate(models.Model):
    region = models.CharField(max_length=8)
    type = models.CharField(max_length=8)
    year = models.IntegerField()
    month = models.CharField(max_length=3)
    data = models.FloatField(null=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "region:{}, type:{}, year:{}, month:{}, data:{}".format(self.region, self.type, self.year, self.month, self.data)
