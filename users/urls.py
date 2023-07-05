from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/', views.getOrUpdateUser), #since we can update and list with same address
    path('users/', views.postUser),
]
