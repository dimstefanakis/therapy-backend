# Generated by Django 3.1.4 on 2020-12-14 02:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='therapist',
            name='surrogate',
            field=models.UUIDField(db_index=True, default=uuid.uuid4),
        ),
    ]