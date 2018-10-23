from django.forms import ModelForm
from django import forms

from boards.models import Post, Bid
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'event_date': DateInput(),
            'end_date': DateInput(),
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
            'budget': forms.TextInput(attrs={'placeholder': 'Enter your budget'}),
            'location': forms.TextInput(attrs={'placeholder':'Enter a suburb'}),
            'comment': forms.TextInput(attrs={'placeholder':'Enter any extra information'}),

        }
        exclude = ('user', 'pub_date', 'winner_selected', 'status')


class BidForm(ModelForm):
    class Meta:
        model = Bid
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'Enter bid amount'}),
            'comment': forms.TextInput(attrs={'placeholder': 'Enter extra information'}),
            'contact_details': forms.TextInput(attrs={'placeholder': 'Enter contact details'})
        }
        exclude = ('user', 'post')




