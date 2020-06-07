# Generated by Django 3.0.6 on 2020-06-04 05:24

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_image_directory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imagefile',
            field=models.FileField(blank=True, default='', upload_to=home.models.UploadedConfigPath, verbose_name=''),
        ),
    ]
