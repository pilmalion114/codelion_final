from django.urls import path

from restaurantapp.views import text

app_name = 'restaurantapp'

urlpatterns = [
    path('', text)
]
