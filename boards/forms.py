from django.forms import ModelForm
from django import forms

from boards.models import Post, Bid


class DateInput(forms.DateInput):
    input_type = 'date'


class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'event_date': DateInput(),
            'end_date': DateInput(),
        }
        exclude = ('user', 'pub_date', 'winner_selected',)


class BidForm(ModelForm):
    class Meta:
        model = Bid
        exclude = ('user', 'post')



SORT_BY= [
    ('most_recent', 'Most Recent'),
    ('budget_ascending', 'Budget (Ascending)'),
    ('budget_descending', 'Budget (Descending)'),
    ('event_date_descending', 'Event Date (Descending)'),
    ('event_date_ascending', 'Event Date (Ascending)'),
    ]

TIME_FILTER = [
    ('this_week', 'This Week'),
    ('this_month', 'This Month'),
]

class OptionsForm(forms.Form):
    sort_option = forms.CharField(label='Filter', widget=forms.RadioSelect(choices=SORT_BY), required=False)
    min_value = forms.FloatField(min_value=0, max_value=100000, required=False)
    max_value = forms.FloatField(min_value=0, max_value=100000, required=False)
    time_range = forms.CharField(label='Time Range', widget=forms.RadioSelect(choices=TIME_FILTER), required=False)

    def is_valid(self):

        print("NEEDS VALIDATION")
        return True

