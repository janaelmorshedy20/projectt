# Generated by Django 4.2.4 on 2023-08-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_signuppage_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='signuppage',
            name='username',
            field=models.CharField(blank=b'I01\n', max_length=20, null=True),
        ),
    ]
