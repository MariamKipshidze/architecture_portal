from django.urls import path
from project.views import project_list, project_detail

urlpatterns = [
    path('', project_list, name='project_list'),
    path('<int:pk>/', project_detail, name='project_detail'),
]
