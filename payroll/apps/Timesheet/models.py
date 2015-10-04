from django.db import models


class Timesheet(models.Model):
    period_start = models.DateField()
    period_end = models.DateField()


class Entry(models.Model):
    date = models.DateField()
    hours = models.TimeField()
    timesheet = models.ForeignKey('Timesheet')
