# Generated by Django 2.1.1 on 2018-10-10 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_remove_post_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidder_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='current_lowest_bid',
        ),
        migrations.RemoveField(
            model_name='post',
            name='starting_price',
        ),
        migrations.AddField(
            model_name='bid',
            name='comment',
            field=models.CharField(default='commetn scomment', help_text='Explaination', max_length=300, verbose_name='Bid Comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='contact_details',
            field=models.CharField(default='04 111 1111111', help_text='Enter Contact Number', max_length=300, verbose_name='Contact Details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='budget',
            field=models.IntegerField(default=100, help_text='Enter your maximum price for the event', verbose_name='Maximum Budget'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.CharField(default='This is a comment', help_text='Explaination', max_length=300, verbose_name='Bid Comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='event date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(default='Coffs Harbour', help_text='Enter Suburb', max_length=100, verbose_name='Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='winnerSelected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Please enter a title for the job post', max_length=200, verbose_name='Post Title'),
        ),
    ]
