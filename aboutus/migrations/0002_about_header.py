# Generated by Django 3.0.6 on 2020-06-03 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='header',
            field=models.CharField(choices=[('Welcome', 'Welcome at Home page'), ('About_Us', 'About us page'), ('Read_More', 'Read more portions')], default='Welcome', max_length=32),
        ),
    ]
