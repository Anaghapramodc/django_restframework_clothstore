from rest_framework import serializers
from .models import cloths, cart


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = cloths
        fields = '__all__'




class  cartSerializer(serializers.ModelSerializer):

    class Meta:
        model = cart
        fields = '__all__'


