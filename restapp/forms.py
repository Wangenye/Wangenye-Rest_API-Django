from django import forms

from .models import Order

class CustomerOrderForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = ('name','amount','order_no','phone')