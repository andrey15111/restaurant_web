from menu.models import *
from datetime import datetime


class OrderController:
    def __init__(self, pk: int = None):
        self.order = None
        if pk:
            self.order = Dish.objects.get(id=pk)

    def _calculate_total_price(self, dishes):
        total_price = 0
        for dish_item in dishes:
            dish = Dish.objects.get(id=dish_item['dish_id'])
            total_price += dish.price * dish_item['count']
        return total_price


    def create(self, user, dishes, restaurant):
        order, created = Order.objects.get_or_create(
                                            username=user,
                                            price_total=self._calculate_total_price(dishes),
                                            date_order=datetime.utcnow(),
                                            restaurant=Restaurant.objects.get(id=restaurant)
                                            )
        self.order = OrderList.objects.create(
            dishes = dishes,
            order = order
        )
        self.order.save()
        return self.order

    def delete(self, order):
        order.delete()
        return True