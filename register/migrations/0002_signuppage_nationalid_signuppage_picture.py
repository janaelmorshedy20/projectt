# Generated by Django 4.2.4 on 2023-08-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signuppage',
            name='nationalid',
            field=models.ImageField(blank=b'I01\n', null=True, upload_to='photos/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='signuppage',
            name='picture',
            field=models.ImageField(blank=b'I01\n', null=True, upload_to='photos/%y/%m/%d'),
        ),
    ]
