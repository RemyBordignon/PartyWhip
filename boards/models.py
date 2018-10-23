from datetime import timezone, datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils import timezone


class Post(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=False, verbose_name="Post Title")
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date')
    event_date = models.DateTimeField('event date')
    budget = models.IntegerField(blank=False, verbose_name="Maximum Budget")
    location = models.CharField(max_length=100, verbose_name="Location")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments")
    winner_selected = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default="OPEN")


    def __str__(self):
        return self.title

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        print(self.end_date)
        if self.end_date >= self.event_date:
            raise ValidationError("Invalid Date: the Event Date must be after the End Date")
        if self.end_date <= timezone.now() or self.event_date <= timezone.now():
            raise ValidationError("Invalid Date: the date you have chosen has passed")


class Bid(models.Model):
    user = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, verbose_name="Bid Price")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments")
    contact_details = models.CharField(max_length=300, verbose_name="Contact Details")

    def __str__(self):
        return str(self.price)
