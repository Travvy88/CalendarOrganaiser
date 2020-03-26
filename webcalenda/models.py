from django.db import models
from django.utils import timezone


class Day(models.Model):
    name = models.CharField(max_length=3)
    week = models.IntegerField()
    weekend = models.BooleanField()
    holiday = models.CharField(max_length=40)
    notes = models.TextField()

    def change_notes(self):
        pass



