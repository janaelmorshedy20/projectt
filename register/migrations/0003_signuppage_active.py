# Generated by Django 4.2.4 on 2023-08-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_signuppage_nationalid_signuppage_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='signuppage',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]