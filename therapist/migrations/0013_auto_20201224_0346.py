# Generated by Django 3.1.4 on 2020-12-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0012_remove_therapysession_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to='licenses/'),
        ),
    ]
