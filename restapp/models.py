from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    image =models.ImageField(upload_to='items/store', null=True)
    description = models.TextField()

    def __str__(self):
        return self.name