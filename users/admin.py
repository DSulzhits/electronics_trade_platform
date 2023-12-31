from django.contrib import admin
from users.models import User


@admin.register(User)
class ElectronicsTradeAdmin(admin.ModelAdmin):
    """Register User model in Admin
    (Модель User зарегистрирована в админке"""
    list_display = ('id', 'email', 'is_active',)
    list_filter = ('id', 'email',)
    ordering = ('id',)
