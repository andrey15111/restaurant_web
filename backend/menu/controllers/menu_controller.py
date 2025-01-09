from menu.models import *
from datetime import datetime


class MenuController:
    def __init__(self, pk: int = None):
        self.menu = None
        if pk:
            self.menu = Menu.objects.get(id=pk)

    def create(self, name, restaurant):
        self.menu = Menu.objects.create(
            name=name,
            date_updated=datetime.utcnow(),
            restaurant = restaurant
        )
        self.menu.save()
        return self.menu
    
    def edit(self, name):
        self.menu.name = name
        self.menu.date_updated=datetime.utcnow(),
        self.menu.save()
        return self.menu

    def delete(self, menu):
        menu.delete()
        return True
