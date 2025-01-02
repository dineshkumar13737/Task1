import pytest
from core.models import Organization, Role, User

@pytest.mark.django_db
def test_organization_creation():
    organization = Organization.objects.create(name="Test Org", description="Test Description")
    assert organization.name == "Test Org"
    assert organization.description == "Test Description"
    assert organization.created_at is not None

@pytest.mark.django_db
def test_role_creation():
    organization = Organization.objects.create(name="Test Org", description="Test Description")
    role = Role.objects.create(name="Test Role", description="Test Role Description", organization=organization)
    assert role.name == "Test Role"
    assert role.organization == organization

@pytest.mark.django_db
def test_user_creation():
    organization = Organization.objects.create(name="Test Org", description="Test Description")
    user = User.objects.create_user(username="testuser", email="testuser@example.com", password="password123", organization=organization)
    assert user.username == "testuser"
    assert user.email == "testuser@example.com"
    assert user.organization == organization