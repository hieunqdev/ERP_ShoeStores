# Generated by Django 4.1.1 on 2022-10-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktime',
            name='end_day',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='start_day',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
