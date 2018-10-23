from datetime import timezone, datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError


class Post(models.Model):
    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=False, verbose_name="Post Title", help_text="Please enter a title for the job post")
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date')
    event_date = models.DateTimeField('event date')
    budget = models.IntegerField(blank=False, verbose_name="Maximum Budget", help_text="Enter your maximum price for the event")
    location = models.CharField(max_length=100, verbose_name="Location", help_text="Enter Suburb")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments", help_text="Enter extra information")
    winner_selected = models.BooleanField(default=False)
    status = models.CharField(max_length=10, default="OPEN")

    def __str__(self):
        return self.title

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.end_date > self.event_date:
            raise ValidationError(('Bidding close must be before event date.'))

class Bid(models.Model):
    user = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, verbose_name="Bid Price", help_text="Please enter your bid amount")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments", help_text="Enter extra information")
    contact_details = models.CharField(max_length=300, verbose_name="Contact Details", help_text="Enter Contact Number")

    def __str__(self):
        return str(self.price)
