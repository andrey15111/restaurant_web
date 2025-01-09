import pytest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest.serializers.core import LoginSerializer
from rest.viewsets.auth import AuthViewSet
from rest_framework.response import Response
from unittest.mock import Mock, patch

@pytest.fixture
def user():
    """Создание тестового пользователя."""
    return User.objects.create_user(username="admin", password="1")


@pytest.mark.django_db
def test_login_serializer_valid():
    """Тест сериализатора: корректные данные."""
    data = {"username": "test_user", "password": "password123"}
    serializer = LoginSerializer(data=data)
    assert serializer.is_valid(), "Сериализатор должен быть валидным для корректных данных."


@pytest.mark.django_db
def test_login_serializer_invalid():
    """Тест сериализатора: некорректные данные."""
    data = {"username": "test_user"}  # Отсутствует пароль
    serializer = LoginSerializer(data=data)
    assert not serializer.is_valid(), "Сериализатор не должен быть валидным при отсутствии пароля."
    assert "password" in serializer.errors, "Ошибки сериализатора должны содержать ключ 'password'."


@pytest.mark.django_db
def test_auth_viewset_login_success():
    """Изолированный тест успешной авторизации через AuthViewSet."""
    # Создаем фиктивный запрос с данными
    request_data = {"username": "admin", "password": "1"}
    mock_request = Mock()
    mock_request.data = request_data

    # Мокаем функции authenticate и login
    with patch("rest.viewsets.auth.authenticate") as mock_authenticate, \
         patch("rest.viewsets.auth.login") as mock_login:

        # Настраиваем `authenticate` для возврата фиктивного пользователя
        mock_user = Mock()
        mock_user.is_active = True
        mock_authenticate.return_value = mock_user

        # Создаем экземпляр ViewSet и вызываем метод login
        viewset = AuthViewSet()
        response = viewset.login(mock_request)

        # Проверяем, что authenticate вызван с правильными параметрами
        mock_authenticate.assert_called_once_with(username="admin", password="1")
        
        # Проверяем, что login вызван с корректными аргументами
        mock_login.assert_called_once_with(mock_request, mock_user)

        # Проверяем, что метод вернул статус 202
        assert isinstance(response, Response)
        assert response.status_code == 202, "Ожидается статус 202 для успешной авторизации."


@pytest.mark.django_db
def test_auth_viewset_login_failure(user):
    """Тест авторизации с неправильными учетными данными."""
    viewset = AuthViewSet()
    request_data = {"username": "admin", "password": "wrongpassword"}
    request = type("Request", (), {"data": request_data, "user": None})
    
    # Переопределяем метод `authenticate` для тестирования
    def mock_authenticate(username, password):
        return None

    viewset.authenticate = mock_authenticate
    response = viewset.login(request)
    assert response.status_code == 403, "Ожидается статус 403 для неправильных данных."
    assert response.data == "Не верные данные для авторизации.", "Сообщение об ошибке должно быть корректным."


@pytest.mark.django_db
def test_auth_viewset_login_inactive_user():
    """Тест авторизации неактивного пользователя."""
    user = User.objects.create_user(username="inactive_user", password="password123", is_active=False)
    viewset = AuthViewSet()
    request_data = {"username": "inactive_user", "password": "password123"}
    request = type("Request", (), {"data": request_data, "user": None})
    
    # Переопределяем метод `authenticate` для тестирования
    def mock_authenticate(username, password):
        return user if username == "inactive_user" and password == "password123" else None

    viewset.authenticate = mock_authenticate
    response = viewset.login(request)
    assert response.status_code == 403, "Ожидается статус 403 для неактивного пользователя."
    assert response.data == "Не верные данные для авторизации.", "Сообщение об ошибке должно быть корректным."
