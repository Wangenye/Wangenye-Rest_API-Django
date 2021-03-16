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
class Order(models.Model):
    order = models.ForeignKey(Item,on_delete=models.CASCADE,related_name="items")
    timestamp = models.DateTimeField(auto_now_add=True)
    order_no = models.CharField(max_length=10,default=generate_order_no)

    class Meta:
        unique_together = ['order','timestamp']
        ordering = ['timestamp']

    def __str__(self):
        return 'Order_no: %s ' % (self.order_no, )