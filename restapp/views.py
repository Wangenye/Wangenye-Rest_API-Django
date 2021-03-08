from django.shortcuts import render
from  .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status , permissions
from .serializer import ItemSerializer


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