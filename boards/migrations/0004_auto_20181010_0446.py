# Generated by Django 2.1.1 on 2018-10-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20181010_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='winnerSelected',
            new_name='winner_selected',
        ),
        migrations.AlterField(
            model_name='bid',
            name='comment',
            field=models.CharField(help_text='Enter extra information', max_length=300, verbose_name='Bid Comments'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.IntegerField(help_text='Please enter your bid amount', verbose_name='Bid Price'),
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(help_text='Enter extra information', max_length=300, verbose_name='Bid Comments'),
        ),
    ]