from django.contrib import admin
from suppliers.models import ChainElement, Product


@admin.action(description="Clear debt summ")
def clear_summ(modeladmin, request, queryset):
    """Add admin action, which allows you to reset your debt to 0
    (Добавлена admin action, которая позволяет сбросить долг до 0"""
    queryset.update(debt=0)


@admin.register(ChainElement)
class ChainElementAdmin(admin.ModelAdmin):
    """Register ChainElement model in Admin
    (Модель ChainElement зарегистрирована в админке"""
    list_display = ('id', 'supplier', 'name', 'debt',)
    list_filter = ('id', 'city',)
    ordering = ('id',)
    actions = [clear_summ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Register Product model in Admin
    (Модель Product зарегистрирована в админке"""
    list_display = ('id', 'name', 'model', 'seller',)
    list_filter = ('id', 'name',)
    ordering = ('id',)
