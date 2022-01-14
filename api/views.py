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
                data=list(Product.objects.values('prod_id','prod_name_ta','prod_desc_ta','prod_class_ta'))
                for i in data:
                    i['prod_name']=i.pop('prod_name_ta')
                    i['prod_class']=i.pop('prod_class_ta')
                    i['prod_desc']=i.pop('prod_desc_ta')
                return JsonResponse(data,safe=False)
            elif (lang_code == 'ka'):
                data=list(Product.objects.values('prod_id','prod_name_ka','prod_desc_ka','prod_class_ka'))
                for i in data:
                    i['prod_name']=i.pop('prod_name_ka')
                    i['prod_class']=i.pop('prod_class_ka')
                    i['prod_desc']=i.pop('prod_desc_ka')
                return JsonResponse(data,safe=False)
        else:
            data=list(Product.objects.values('prod_id','prod_name_en','prod_desc_en','prod_class_en'))
            for i in data:
                    i['prod_name']=i.pop('prod_name_en')
                    i['prod_class']=i.pop('prod_class_en')
                    i['prod_desc']=i.pop('prod_desc_en')
            return JsonResponse(data,safe=False)
