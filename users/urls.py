from django.urls import include, path
from . import views

urlpatterns = [
    path('users/<int:user_id>/', views.getUser),
    path('users/', views.postUser),
]
