from django.shortcuts import render
import securities.config as static
from django.http import HttpResponseRedirect, HttpResponse

def mainPage(request):
    data={}
    securityList=['10234jdkajs']*100
    data['title']='历史行情' 
    data['main']=static.assets

    data['securityList']=securityList   #receive data as the name says. format as: ['000001中国银行',...]

    return render(request,'securities/main.html',data)

