from django.test import TestCase
from restapp.forms import CustomerOrderForm


class FormTests(TestCase):

    def  test_customerorder_form(self):
        form = CustomerOrderForm(data={
            'name':"Username",
            'amount':"1000",
            'order_no': "Ttyuty01",
            'phone':"2541234567890",
        })
        self.assertTrue(form.is_valid())

    def  test_customerorder_no_form(self):
        form = CustomerOrderForm(data={})
        self.assertEquals(len(form.errors),4)

    