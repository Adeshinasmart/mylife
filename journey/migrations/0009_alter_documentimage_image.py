# Generated by Django 5.0.7 on 2025-01-12 11:26

import django.core.validators
import journey.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0008_remove_documentimage_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentimage',
            name='image',
            field=models.ImageField(upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(['jpeg', 'pdf', 'png']), journey.models.validate_image]),
        ),
    ]
