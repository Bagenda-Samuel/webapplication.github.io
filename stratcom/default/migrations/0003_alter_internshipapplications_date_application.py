# Generated by Django 4.0.5 on 2022-06-29 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_internshipapplications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internshipapplications',
            name='date_application',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
