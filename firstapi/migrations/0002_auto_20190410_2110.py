# Generated by Django 2.1.7 on 2019-04-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='age',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='name',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='phone',
        ),
        migrations.AddField(
            model_name='snippet',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]