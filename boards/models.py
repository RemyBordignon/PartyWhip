from datetime import timezone, datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    # Fields
    title = models.CharField(max_length=200, blank=False, verbose_name="Post Title", help_text="Please enter a title for the job post")
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date')
    event_date = models.DateTimeField('event date')
    budget = models.IntegerField(blank=False, verbose_name="Maximum Budget", help_text="Enter your maximum price for the event")
    location = models.CharField(max_length=100, verbose_name="Location", help_text="Enter Suburb")
    comment = models.CharField(max_length=300, verbose_name="Bid Comments", help_text="Explaination")
    winnerSelected = models.BooleanField(default=False)

    def valid_current_bid(self):
        return self.current_lowest_bid >= self.starting_price

    def bidding_open(self):
        # STUB FOR NOW
        # return time.now() < end_date
        return True

    def __str__(self):
        return self.title


class Bid(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    price = models.IntegerField()
    comment = models.CharField(max_length=300, verbose_name="Bid Comments", help_text="Explaination")
    contact_details = models.CharField(max_length=300, verbose_name="Contact Details", help_text="Enter Contact Number")

    def __str__(self):
        return str(self.price)


