from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from . import serializer
from .models import cloths, cart
from .serializer import ClothSerializer, cartSerializer
from rest_framework import generics, request, status


# Create your views here.

class ListCloths(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClothSerializer
    queryset =cloths.objects.all()

    def list(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = ClothSerializer(queryset,many=True)
        return Response(serializer.data)


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ClothSerializer
    queryset = cloths.objects.all()

    def get(self,request,*args,**kwargs):
        queryset =  self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClothSerializer(queryset,many=False)
        return Response(serializer.data)

class ClothUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = cloths.objects.all()
    serializer_class = ClothSerializer



class ClothDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = cloths.objects.all()
    serializer_class = ClothSerializer




class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        try:
            product = cloths.objects.get(id=product_id)
            cart_item = cart(user=request.user, product=product, quantity=quantity)
            serializer = cartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
