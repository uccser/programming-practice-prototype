# Generated by Django 2.0.4 on 2018-09-22 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0028_badge_id_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='id_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]