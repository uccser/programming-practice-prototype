# Generated by Django 2.0.4 on 2018-05-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]