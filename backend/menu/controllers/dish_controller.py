from menu.models import *

class DishController:
    def __init__(self, pk: int = None):
        self.dish = None
        if pk:
            self.dish = Dish.objects.get(id=pk)

    def create(self, name, price, menu: int):
        self.dish = Dish.objects.create(
            name=name,
            price=price,
            menu=menu
        )
        self.dish.save()
        return self.dish
    
    def edit(self, name, price):
        self.dish.name = name
        self.dish.price = price
        self.dish.save()
        return self.dish

    def delete(self, dish):
        dish.delete()
        return True