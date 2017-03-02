from django.shortcuts import render
import securities.config as static


def mainPage(request):
    data={}
    data['title']='历史行情' 
    data['main']=static.assets 
    return render(request,'securities/main.html',data)