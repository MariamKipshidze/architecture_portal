from django.urls import path
from django.views.generic import TemplateView

from application import views

app_name = 'application'

urlpatterns = [
    path('calculator/', views.calculate_price, name='calculate_price'),
    path('create_application/', views.ApplicationCreateView.as_view(), name='create_application'),
    path('thank-you/', TemplateView.as_view(template_name='thank_you.html'), name='thank_you')
]
