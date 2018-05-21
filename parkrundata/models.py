# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=128)


class Event(TimeStampedModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=256)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)