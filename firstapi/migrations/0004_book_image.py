# Generated by Django 2.1.7 on 2019-04-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapi', '0003_auto_20190410_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
