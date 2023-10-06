from django.contrib import admin
from suppliers.models import ChainElement


@admin.register(ChainElement)
class ChainElementAdmin(admin.ModelAdmin):
    """Register ChainElement model in Admin
    (Модель ChainElement зарегистрирована в админке"""
    list_display = ('id', 'supplier', 'name',)
    list_filter = ('id', 'city',)
    ordering = ('id',)
