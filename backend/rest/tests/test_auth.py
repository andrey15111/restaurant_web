import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

@pytest.fixture
def api_client():
    """Фикстура для API клиента."""
    return APIClient()

@pytest.mark.django_db
def test_login_success(api_client):
    """Тест успешной авторизации."""
    # Создаем пользователя
    User = get_user_model()
    User.objects.create_user(username="admin", password="1")

    # Отправляем запрос на авторизацию
    response = api_client.post(
        "http://172.17.0.3:8000/api/v1/auth/simple/login", 
        {"username": "admin", "password": "1"}
    )

    # Проверяем, что запрос успешен
    assert response.status_code == status.HTTP_202_ACCEPTED

@pytest.mark.django_db
def test_login_failure(api_client):
    """Тест ошибки авторизации с неверными данными."""
    response = api_client.post(
        "http://172.17.0.3:8000/api/v1/auth/simple/login", {"username": "wronguser", "password": "wrongpass"}
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.data == "Не верные данные для авторизации."