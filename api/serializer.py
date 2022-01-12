from django.db.models import fields
from django.http.response import JsonResponse
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = '__all__'
class ProducttaSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields='__all__'
        #fields = ['prod_id','prod_name_ta','prod_desc_ta','prod_class_ta']