from django.urls import path
from .views import get_client,create_client,update_client,delete_client

urlpatterns = [
    path('', get_client, name="clients"),
    path('create/', create_client, name="create_client"),
    path('clients/<int:pk>/update/',update_client, name='update_client'),
    path('clients/<int:pk>/delete/', delete_client, name='delete_client'),
]
    