from django.forms import ModelForm
from django import forms

from django.core.exceptions import ValidationError

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
        exclude = ('user', 'pub_date', 'winner_selected', 'status')


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

def validate_positive(value):
    if value < 0:
        raise ValidationError('Enter positive Value')
    return value


class OptionsForm(forms.Form):
    sort_option = forms.ChoiceField(choices=SORT_BY, widget=forms.RadioSelect(), required=False)
    min_value = forms.FloatField(min_value=0, max_value=100000, required=False, validators=[validate_positive])
    max_value = forms.FloatField(min_value=0, max_value=100000, required=False, validators=[validate_positive])
    time_range = forms.ChoiceField(choices=TIME_FILTER, widget=forms.RadioSelect(), required=False)
