from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('transform/<str:file_name>/', views.transform, name='transform'),
]
