from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="Post Title", help_text="Please enter a title for the job post")
    #poster = models.ForeignKey(User, related_name="poster", on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    #NEED AN END DATE
    starting_price = models.IntegerField(blank=False, verbose_name="Starting Price", help_text="Enter the starting price for this job")
    current_lowest_bid = models.IntegerField()

    def valid_current_bid(self):
        return self.current_lowest_bid >= self.starting_price

    def __str__(self):
        return self.title


class Bid(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # leave basic for now, update to user
    bidder_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return str(self.price)


