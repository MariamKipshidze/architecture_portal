from django.urls import path
from application import views

urlpatterns = [
    path('calculator/', views.calculate_price, name='calculate_price'),
]
