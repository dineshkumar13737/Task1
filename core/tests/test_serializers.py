import pytest
from core.models import Organization
from core.serializers import OrganizationSerializer

@pytest.mark.django_db
def test_organization_serializer_validation():
    organization_data = {
        "name": "Test Org",
        "description": "Test Description"
    }
    serializer = OrganizationSerializer(data=organization_data)
    assert serializer.is_valid()
    assert serializer.validated_data["name"] == "Test Org"