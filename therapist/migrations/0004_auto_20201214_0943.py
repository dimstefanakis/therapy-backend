# Generated by Django 3.1.4 on 2020-12-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0003_therapysession'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapysession',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='therapysession',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
