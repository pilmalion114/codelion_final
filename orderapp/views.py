from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from orderapp.forms import OrderCreateForm, MenuChoiceForm
from orderapp.models import Order, OrderMenu



# 음식 선택
def menu_choice(request):
    return render(request, 'orderapp/menu_choice.html', {'menu':'example'})

# 주문 생성
def order_create(request):
    return render(request, 'orderapp/order_create.html')

def cash(request):
    return render(request, 'orderapp/cash.html')

def credit_card(request):
    return render(request, 'orderapp/credit_card.html')

def transfer(request):
    return render(request, 'orderapp/transfer.html')

def base3(request):
    return render(request, 'orderapp/chicken_detailPage.html')

def cash(request):
    return render(request, 'orderapp/cash.html')

def order_report(request):
    return render(request, 'orderapp/order_report.html')