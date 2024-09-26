from django.db import models
from django.forms import ModelForm

from orderapp.models import Order
from restaurantapp.models import Menu, Restaurant


def remaining_time(delivery_time, restaurant_id):
    receipt_complete_count = Order.objects.filter(restaurant_id=restaurant_id, status='접수 완료').count() // 3
    delivery_time += receipt_complete_count * (delivery_time // 2)
    return f'{delivery_time}~{delivery_time + 10}분'


class MenuDetailForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'image', 'caption', 'price', 'option_group')


class MenuListForm(ModelForm):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'image', 'caption', 'menu_group_id', 'price')


class RestaurantDetailForm(ModelForm):
    delivery_time = models.CharField()

    def get_delivery_time(self, obj):
        return remaining_time(obj.delivery_time, obj.id)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'image', 'open_time', 'close_time', 'tel_number', 'address',
                  'min_order_price', 'payment_methods', 'business_name', 'company_registration_number',
                  'origin_information', 'allergy_notification', 'delivery_charge', 'delivery_time', 'reorder_count')


class RestaurantListForm(ModelForm):
    delivery_time = models.CharField()
    reorder_count = models.IntegerField()

    def get_delivery_time(self, obj):
        return remaining_time(obj.delivery_time, obj.id)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'reorder_count', 'image', 'delivery_charge', 'delivery_time', 'min_order_price')

