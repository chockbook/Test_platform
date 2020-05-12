from django.shortcuts import render
import requests

def ApiTest(request,queryset):
    
    url = queryset.api_test_url #地址
    value = queryset.api_test_value #参数
    #header = queryset.header #请求头
    method = queryset.api_test_method  #请求方式
    #print(url)
    #print(value)
  
    #print(method)
    if method == "get":
       
        response  = requests.get(url,params=value)
        result = response.json()
       

    if method == "post":
        response = requests.post(url,params=value)
        result = response.json()
        
    return result




# Create your views here.
