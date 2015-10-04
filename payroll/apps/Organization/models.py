from django.db import models




class Organization(models.Model):
    name = models.CharField(max_length=100)


class Employee(models.Model):
    user = models.OneToOneField(User)
    organization = models.ForeignKey('Organization')
