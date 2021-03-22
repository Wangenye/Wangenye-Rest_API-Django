from django.shortcuts import render,get_object_or_404,redirect
import africastalking
# from okta_oauth2.decorators import okta_login_required
from  .models import Item,Order
# from customerApp.models import UserProfile
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status , permissions
from .serializer import ItemSerializer, OrderedItems,CustomerSerializer
from .forms import CustomerOrderForm
import random, string
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()


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

        serializer = ItemSerializer(items,many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)
class CustomerApiView(APIView):
    # permission_classes = [permission_classes]

    def get (self,request,*args, **kwargs):
        customer = User.objects.all()
       
        serializer = CustomerSerializer(customer,many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)
# @okta_login_required
class OrderApi(APIView):
    # permission_classes = [permission_classes]

    def get (self,request,*args, **kwargs):
        # items = Item.objects.all()
        order = Order.objects.order_by('-timestamp')

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

            # print(item.phone)

            
            return redirect("order_detail")
        else:
            print("Error")
    else:
        form = CustomerOrderForm()
            # order = form.save(commit=False)
            # order.item = item

    

    return render(request,'restapp/orderpage.html',{'form':form,'item':item,'order_no':order_no})

def OrderDetails(request):
    # orderdetail = get_object_or_404(Order,pk=order_id)
    all_orders = Order.objects.order_by('-timestamp')[:1]

    return render(request,"restapp/order_detail.html",{"all_orders":all_orders})

def ConfirmOrder(request,order_id):
    confirm = get_object_or_404(Order,pk=order_id)
    username = "sandbox"
    api_key ="c110a50034b61d4deb579bd45053013a9a647d896106c5d617ea986f2e6a565d"  
    # api_key = env('API_KEY')
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    User= request.user
    phone_no = confirm.phone
    print(confirm.name)
    response = sms.send("Hello {}\n Your item --{}-- has been Ordered succesfully!\n Order No: {}.\n Time Ordered: {}".format(User,confirm.name,confirm.order_no,confirm.timestamp), [phone_no])

    # return render(request,'restapp/checkout.html',{'confirm':confirm})
    return redirect("/")


# def SendSms(request,id):
#     confirm = get_object_or_404(Order,pk=order_id)

#     print(confirm.phone)

#     username = "sandbox"
#     api_key ="c110a50034b61d4deb579bd45053013a9a647d896106c5d617ea986f2e6a565d"  
#     africastalking.initialize(username, api_key)
#     sms = africastalking.SMS
#     User= request.user
#     response = sms.send("Hello {}\n. Your item has been Ordered succesfully!\n Order No: {}.\n Time Ordered: {}".format(User,confirm.order_no,confirm.timestamp), ["+254726869778"])
#     return redirect("/")


