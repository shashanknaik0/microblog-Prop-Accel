from django.urls import path
from . import views

urlpatterns = [
    #as specified in the question to use same path for Get, update, delete request
    path('posts/<int:post_id>/', views.getUpdateOrDeletePost),
    path('posts/', views.getAllAndCreatePost),
]
