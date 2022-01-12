from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import fields
from rest_framework.views import APIView
from .serializer import ProductSerializer,ProducttaSerializer
from .models import Product
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView, RetrieveAPIView,UpdateAPIView
import json
# Create your views here.
class prodListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class prodcreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class getAPIVIEW(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class tamilresults(APIView):
    def get(self,request):
        data = Product.objects.values('prod_id','prod_name_ta','prod_desc_ta','prod_class_ta')
        
        return JsonResponse(list(data),safe=False)

class getdata(APIView):
    def get(self,request):
        allowed_langs = ['ta','ka']
        lang_code = request.GET.get('lang_code')
        if(lang_code in allowed_langs):
            if(lang_code=='ta'):
                return JsonResponse(list(Product.objects.values('prod_id','prod_name_ta','prod_desc_ta','prod_class_ta')),safe=False)
            elif (lang_code == 'ka'):
                return JsonResponse(list(Product.objects.values('prod_id','prod_name_ka','prod_desc_ka','prod_class_ka')),safe=False)
        else:
            return JsonResponse(list(Product.objects.values('prod_id','prod_name_en','prod_desc_en','prod_class_en')),safe=False)
