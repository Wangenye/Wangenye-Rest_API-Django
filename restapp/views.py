from django.shortcuts import render,get_object_or_404,redirect
from  .models import Item,Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status , permissions
from .serializer import ItemSerializer, OrderedItems
from .forms import CustomerOrderForm
import random, string


# Create your views here.
def IndexPage(request):
    return render(request,'restapp/base.html')

def ItemsPage(request):
    items = Item.objects.all()

    return render(request,'restapp/items.html',{'items':items})


class ItemApiView(APIView):
    # permission_classes = [permission_classes]

    def get (self,request,*args, **kwargs):
        items = Item.objects.all()
        order = Order.objects.all()

        sorder = OrderedItems(order,many=True)
        serializer = ItemSerializer(items,many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)

class OrderApi(APIView):
    # permission_classes = [permission_classes]

    def get (self,request,*args, **kwargs):
        # items = Item.objects.all()
        order = Order.objects.all()

        # sorder = OrderedItems(order,many=True)
        serializer = OrderedItems(order,many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)

# def MakeOrder(request,id):
#     item = get_object_or_404(Order,pk=id)

def OrderPage(request,item_id,):
    # item = Item.objects.get(pk=item_id)
    x = ''.join(random.choice(string.ascii_uppercase  + string.digits) for _ in range(8))
    item = get_object_or_404(Item,pk=item_id)
    order_no = x+"#{}".format(item_id)
    # orderdetail = get_object_or_404(Order,pk=order_id)

    if request.method== "POST":
        form = CustomerOrderForm(request.POST)

        if form.is_valid():
            saveorder =form.save(commit=False)
            saveorder.order = item
            saveorder.save()

            # return redirect("order_detail")
        else:
            print("Error")
    else:
        form = CustomerOrderForm()
            # order = form.save(commit=False)
            # order.item = item

    

    return render(request,'restapp/orderpage.html',{'form':form,'item':item,'order_no':order_no})

def OrderDetails(request,order_id):
    orderdetail = get_object_or_404(Order,pk=order_id)

    return render(request,"restapp/order_detail.html",{"orderdetail":orderdetail})

