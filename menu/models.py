from django.db import models

class items(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    components=models.CharField(max_length=100)
    images=models.ImageField(upload_to='photos/%y/%m/&d')
    active=models.BooleanField(default=True)
