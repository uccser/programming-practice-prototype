# Generated by Django 2.1.5 on 2020-06-07 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='title_templated',
            field=models.BooleanField(default=False),
        ),
    ]
