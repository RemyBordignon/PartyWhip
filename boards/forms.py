from django.forms import ModelForm

from boards.models import Post, Bid


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('pub_date', 'current_lowest_bid',)


class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ()
