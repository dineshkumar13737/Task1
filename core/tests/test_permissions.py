import pytest
from rest_framework.test import APIRequestFactory
from core.permissions import IsSuperAdmin
from core.models import User

@pytest.mark.django_db
def test_superadmin_permission():
    factory = APIRequestFactory()
    user = User.objects.create_superuser(username="superadmin", email="superadmin@example.com", password="password123")
    request = factory.get('/api/')
    request.user = user
    permission = IsSuperAdmin()
    assert permission.has_permission(request, None)