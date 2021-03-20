from django.db import models
import random, string

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.CharField(max_length=100)
    image =models.ImageField(upload_to='items/store', null=True)
    description = models.TextField()

    def __str__(self):
        return self.name

generate_order_no = ''.join(random.choice(string.ascii_uppercase  + string.digits) for _ in range(8))

# class CustomerOrder(models.Model):
#      name = models.CharField(max_length=255)
#      phone_number = models.CharField(max_length=13)

class Order(models.Model):
    order = models.ForeignKey(Item,on_delete=models.CASCADE,related_name="items")
    name = models.CharField(max_length=255,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=100,null=True)
    order_no = models.CharField(max_length=10,default=generate_order_no)
    phone = models.CharField(max_length=13,null=True)

    class Meta:
        unique_together = ['order','timestamp']
        ordering = ['timestamp']

    def __str__(self):
        return '%s: %s ' % (self.order_no,self.timestamp )