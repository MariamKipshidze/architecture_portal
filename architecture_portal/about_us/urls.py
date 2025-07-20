from django.urls import path
from about_us.views import contact_view, TeamListView

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('team_members/', TeamListView.as_view(), name='team_list'),
]
