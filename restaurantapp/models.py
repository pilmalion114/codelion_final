from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Category(models.TextChoices):
    ONE = '1인분'
    JAPANESE = '일식'
    CHINESE = '중식'
    CHICKEN = '치킨'
    KOREAN = '한식'
    CAFE = '카페디저트'
    SNACK = '분식'
    PIZZA = '피자'
    WESTERN = '양식'
    MEAT = '고기구이'
    ASIAN = '아시안'
    FASTFOOD = '패스트푸드'
    MIDNIGHT = '야식'
    LUNCHBOX = '도시락'
    VEGAN = '채식'


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    payment_methods = models.CharField(max_length=255) #list
    delivery_time = models.PositiveIntegerField()
    delivery_charge = models.PositiveIntegerField()
    min_order_price = models.PositiveIntegerField()
    categories = models.CharField(max_length=20) #list
    reorder_count = models.PositiveIntegerField(default=0) #재주문횟수

    image = models.ImageField(upload_to='restaurant_image', null=True, blank=True)
    business_name = models.CharField(max_length=255)
    company_registration_number = models.CharField(max_length=255)
    open_time = models.TimeField()
    close_time = models.TimeField()
    tel_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    origin_information = models.TextField()
    allergy_notification = models.TextField()

    def __str__(self):
        return f'({self.id}){self.name}'


def menu_img_path(instance, filename):
    filename = filename.split('?')[0]
    return f'menu_img/{filename}'


class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu_image', null=True, blank=True, max_length=400)
    caption = models.CharField(max_length=255)
    price = models.PositiveIntegerField()


