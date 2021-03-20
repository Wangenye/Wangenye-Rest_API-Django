from rest_framework import  serializers
from .models import  Item,Order

class ItemSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)
    class Meta:
        model = Item
        fields = ["name","amount","description","image",'items']


class OrderedItems(serializers.ModelSerializer):
    # details = serializers.RelatedField(source='details.name',read_only=True)
    # details = serializers.RelatedField(read_only=True,source='details.name')
    # order = serializers.StringRelatedField(many=True,source='order.name')
    class Meta:
        model = Order
        fields = ['name',"amount","order_no","timestamp"]