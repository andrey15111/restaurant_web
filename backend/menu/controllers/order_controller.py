from menu.models import *

class OrderController:
    def __init__(self, pk: int = None):
        self.order = None
        if pk:
            self.order = Dish.objects.get(id=pk)

    def create(self, name, price, menu: int):
        self.order = Dish.objects.create(
            username=user,
            date_ordered=date_ordered,
            price_total = price_total,
            restaurant = restaurant
        )
        self.order.save()
        return self.order
    
    def edit(self, name, price):
        self.order.name = name
        self.order.price = price
        self.order.save()
        return self.order

    def delete(self, order):
        order.delete()
        return True