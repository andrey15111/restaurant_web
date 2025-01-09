from django.contrib import admin

from core.models import Menu, AuthModel,Order,Restaurant, Dish, OrderList


@admin.register(AuthModel)
class AuthModelAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']