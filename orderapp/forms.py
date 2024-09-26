from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm

from orderapp.models import Order, OrderMenu, OrderOption, OrderOptionGroup

# 음식 선택
class MenuChoiceForm(ModelForm):

    class Meta:
        model = OrderMenu
        fields = ('id', 'menu', 'name', 'price', 'count')
        # 메뉴 이름, 가게 이름, 가격, 음식 개수
        # 결제 버튼 (장바구니 생략)

''' 주문 기록
class OrderListForm(ModelForm):
    order_menu = OrderMenuForm
    restaurant_name = models.CharField(source='restaurant.name')
    restaurant_image = models.ImageField(source='restaurant.image')

    class Meta:
        model = Order
        fields = ('id', 'order_menu', 'restaurant_name', 'restaurant_image')'''

# 주문 생성
class OrderCreateForm(ModelForm):
    order_menu = MenuChoiceForm

    class Meta:
        model = Order
        fields = ('id', 'payment_method', 'month_total_price')

    '''def validate(self, attrs):
        if attrs['total_price'] < attrs['restaurant'].min_order_price:
            raise ValidationError('total price < restaurant min price')

        self.total_price = 0
        order_menus = attrs['order_menu']
        for order_menu in order_menus:
            self.valid_order_menu(order_menu)

        restaurant = attrs['restaurant']
        delivery_charge = restaurant.delivery_charge if restaurant.delivery_charge is not None else 0
        discount = restaurant.delivery_discount if restaurant.delivery_discount is not None else 0

        if attrs['total_price'] != self.total_price + delivery_charge - discount:
            raise ValidationError('total price != check_price')

        return attrs

    def create(self, validated_data):
        order_menus = validated_data.pop('order_menu')
        order = Order.objects.create(**validated_data)
        for order_menu in order_menus:
            order_option_groups = order_menu.pop('order_option_group')
            order_menu_obj = OrderMenu.objects.create(order=order, **order_menu)
            for order_option_group in order_option_groups:
                order_options = order_option_group.pop('order_option')
                order_option_group_obj = OrderOptionGroup.objects.create(order_menu=order_menu_obj,
                                                                         **order_option_group)
                for order_option in order_options:
                    OrderOption.objects.create(order_option_group=order_option_group_obj, **order_option)
        return order

    def valid_order_menu(self, order_menu):
        menu = order_menu['menu']
        if order_menu['name'] != menu.name:
            raise ValidationError('menu.name != model menu.name')
        if order_menu['price'] != menu.price:
            raise ValidationError('menu.price != model menu.price')

        menu_price = order_menu['price']

        menu_price = menu_price * order_menu['count']
        self.total_price += 'menu_price' '''
