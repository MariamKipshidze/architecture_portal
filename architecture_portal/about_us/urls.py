from django.urls import path
from about_us.views import contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
]
