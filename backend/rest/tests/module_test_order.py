import pytest
from menu.models import Order, Restaurant, User
from rest.serializers.core import OrderSerializer

@pytest.mark.django_db
def test_order_creation():
    """Тест создания объекта заказа через модель."""
    restaurant = Restaurant.objects.create(
        owner="test_owner",
        time_start_day="08:00:00",
        time_end_day="22:00:00",
        work_days=["MON", "TUE"],
        address="Test Address",
        name="Test Restaurant"
    )
    user = User.objects.create(username="test_user", email="test@test.com")
    order = Order.objects.create(username=user, price_total=100.0, restaurant=restaurant)
    
    assert Order.objects.count() == 1
    assert order.price_total == 100.0
    assert order.restaurant.name == "Test Restaurant"

@pytest.mark.django_db
def test_order_serializer_validation():
    """Тест валидации сериализатора заказа."""
    data = {
        "username": 1,  # Это ID пользователя
        "price_total": 150.0,
        "restaurant": 1  # Это ID ресторана
    }
    serializer = OrderSerializer(data=data)
    assert not serializer.is_valid(), "Сериализатор не должен быть валиден без соответствующих объектов"
    
    # Создаем связанные объекты для корректной валидации
    restaurant = Restaurant.objects.create(
        owner="test_owner",
        time_start_day="08:00:00",
        time_end_day="22:00:00",
        work_days=["MON", "TUE"],
        address="Test Address",
        name="Test Restaurant"
    )
    user = User.objects.create(username="test_user", email="test@test.com")
    data["username"] = user.id
    data["restaurant"] = restaurant.id

    serializer = OrderSerializer(data=data)
    assert serializer.is_valid(), "Сериализатор должен быть валиден с корректными данными"
    validated_data = serializer.validated_data
    assert validated_data["price_total"] == 150.0