import pytest
from rest_framework.test import APIClient
from rest_framework import status
from menu.models import Restaurant, User, Dish, Order

def create_test_user():
    return User.objects.create_user(username="admin", password="1")

def create_test_restaurant():
    return Restaurant.objects.create(
        owner="Test Owner",
        time_start_day="08:00:00",
        time_end_day="22:00:00",
        work_days=["MON", "TUE"],
        address="Test Address",
        name="Test Restaurant"
    )

def create_test_dish(menu):
    return Dish.objects.create(name="Test Dish", price=10.0, menu=menu)

@pytest.mark.django_db
def test_create_order_api():
    """API тест для создания заказа."""
    client = APIClient()
    user = create_test_user()
    restaurant = create_test_restaurant()

    client.login(username="admin", password="1")

    data = {
    "username": user.id,  # Добавьте ссылку на ID пользователя
    "price_total": 50.0,
    "restaurant": restaurant.id
    }

    response = client.post("http://172.17.0.3:8000/api/v1/order/order", data, format="json")
    print(response.status_code)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED, "Ожидался статус 201 при успешном создании заказа"
    assert "id" in response.data, "Ответ должен содержать ID созданного заказа"
    assert response.data["price_total"] == 50.0, "Итоговая цена заказа должна совпадать"
    assert response.data["restaurant"] == restaurant.id, "ID ресторана в заказе должен совпадать"

@pytest.mark.django_db
def test_create_order_unauthenticated():
    """API тест для создания заказа без авторизации."""
    client = APIClient()
    restaurant = create_test_restaurant()

    data = {
        "price_total": 50.0,
        "restaurant": restaurant.id
    }

    response = client.post("http://172.17.0.3:8000/api/v1/order/order", data, format="json")

    assert response.status_code == status.HTTP_403_FORBIDDEN, "Ожидался статус 403 при попытке создания заказа без авторизации"
    assert "detail" in response.data, "Ответ должен содержать описание ошибки"

@pytest.mark.django_db
def test_get_order_list_api():
    """API тест для получения списка заказов."""
    client = APIClient()
    user = create_test_user()
    restaurant = create_test_restaurant()

    # Создаем тестовые заказы
    Order.objects.create(username=user, price_total=100.0, restaurant=restaurant)
    Order.objects.create(username=user, price_total=200.0, restaurant=restaurant)

    client.login(username="admin", password="1")

    response = client.get("http://172.17.0.3:8000/api/v1/order/order")

    assert response.status_code == status.HTTP_200_OK, "Ожидался статус 200 при получении списка заказов"
    assert len(response.data) == 2, "Должно быть возвращено два заказа"
    assert response.data[0]["price_total"] == 100.0, "Первый заказ должен иметь правильную итоговую цену"
    assert response.data[1]["price_total"] == 200.0, "Второй заказ должен иметь правильную итоговую цену"
