from django.urls import include, path
from . import views

urlpatterns = [
    path('users/<int:user_id>/', views.getOrUpdateUser),
    path('users/', views.postUser),
]
