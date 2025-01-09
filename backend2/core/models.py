from django.db import models

from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class AuthModel(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('admin', 'Administrator'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.role

    class Meta:
        managed = False

class Restaurant(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    owner = models.CharField(max_length=100)
    time_start_day = models.TimeField()  # Время открытия
    time_end_day = models.TimeField()  # Время закрытия
    work_days = MultiSelectField(choices=DAYS_OF_WEEK)  # Поле для выбора рабочего дня
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'menu_restaurant'

class Menu(models.Model):
    name = models.CharField(max_length=100)
    date_updated = models.DateTimeField(auto_now_add=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'menu_menu'

class Dish(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'menu_dish'

class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)
    price_total = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'menu_order'

class OrderList(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="orderlist")
    dishes = models.JSONField(default=list)

    class Meta:
        managed = False
        db_table = 'menu_orderlist'