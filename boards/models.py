from datetime import timezone, datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils import timezone

from boards.date import Date


class Post(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=False, verbose_name="Post Title")
    pub_date = models.DateTimeField('Date Published')
    end_date = models.DateTimeField('Bidding Close Date')
    event_date = models.DateTimeField('Event Date')
    budget = models.IntegerField(blank=False, verbose_name="Maximum Budget")
    location = models.CharField(max_length=100, verbose_name="Location")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments")
    winner_selected = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default="OPEN")
    winning_bid = models.IntegerField(default=-1)

    def __str__(self):
        return self.title

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        end_date = Date(self.end_date.day, self.end_date.month, self.end_date.year)
        event_date = Date(self.event_date.day, self.event_date.month, self.event_date.year)
        curr_date = Date(timezone.now().day, timezone.now().month, timezone.now().year)

        if end_date.greaterThan(event_date):
            raise ValidationError("Invalid Date: the Event Date must be after the End Date")
        if not end_date.greaterThan(curr_date) or not event_date.greaterThan(curr_date):
            raise ValidationError("Invalid Date: the date you have chosen has passed")


class Bid(models.Model):
    user = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, verbose_name="Bid Price")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments")
    contact_details = models.CharField(max_length=300, verbose_name="Contact Details")

    def __str__(self):
        return str(self.price)
