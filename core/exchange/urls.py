from django.urls import path
from . import views

urlpatterns = [
    path('price/', views.get_price),
    path('wallet/', views.get_wallet),
    path('buy/', views.buy_doge),
    path('sell/', views.sell_doge),
]