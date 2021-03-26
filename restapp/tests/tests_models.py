from django.test import TestCase
from restapp.models import Item
from restapp.forms import CustomerOrderForm

# Create your tests here.

#model test

class ItemTest(TestCase):

    def create_item(self,name="Item testing",amount=" 000",image="no image",description="Show Description"):
        return Item.objects.create(name=name,amount=amount,image=image,description=description)

    def test_item_creation(self):
        w = self.create_item()
        self.assertTrue(isinstance(w, Item))
        self.assertEqual(w.name,"Item testing")
