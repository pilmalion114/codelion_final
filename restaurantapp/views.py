from django.shortcuts import render

def text(request):
    return render(request,"restaurantapp/text.html")