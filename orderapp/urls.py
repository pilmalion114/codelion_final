from django.urls import path

from orderapp.views import cash, credit_card, transfer, menu_choice, order_create,base3,cash,order_report


app_name = 'orderapp'

urlpatterns = [
    path('menu_choice/', menu_choice, name='menu_choice'),
    path('order_create/', order_create, name='order_create'),
    path('cash/', cash, name='cash'),
    path('credit_card/', credit_card, name='credit_card'),
    path('transfer/', transfer, name='transfer'),
    path('base3/', base3, name='base3'),
    path('cash/', cash, name='cash'),
    path('order_report/', order_report, name='order_report'),

]