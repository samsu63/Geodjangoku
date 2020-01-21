from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models


class Point(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    points = models.PointField(srid=4326)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Points"

# Create your models here.
