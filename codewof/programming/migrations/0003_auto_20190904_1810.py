# Generated by Django 2.1.5 on 2019-09-04 06:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('programming', '0002_auto_20190813_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(max_length=100, unique=True)),
                ('display_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('icon_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Earned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Badge')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='attempt',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='earned_badges',
            field=models.ManyToManyField(through='programming.Earned', to='programming.Badge'),
        ),
    ]