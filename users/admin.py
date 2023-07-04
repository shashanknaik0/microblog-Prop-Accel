from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    #these fieldwill vi visible in admin page
    list_display = ["id", "username", "email", "password"]

#register to django admin page
admin.site.register(User, UserAdmin)