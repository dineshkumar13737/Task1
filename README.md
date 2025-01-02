Overview:

* This Django project is a role-based access control system for managing organizations, roles, and users. It includes three main components.

* Organizations: Represents an organization.

Roles: Represents roles assigned to users within an organization.

Users: Represents users belonging to an organization and assigned specific roles.

Prerequisites:

* Python 3.12

* Django 5

* Django REST Framework

Setup Instructions:

1. Clone the repository:
git clone https://github.com/dineshkumar13737/Task1.git
cd Task1

2. Install dependencies:
pip install -r requirements.txt.

3. Apply migrations:
python manage.py migrate.

4. Run the development server:
python manage.py runserver.

5. Create a superuser:
python manage.py createsuperuser.

API Endpoints:

Organization:

* List Organizations: GET /api/organizations/

* Create Organization: POST /api/organizations/

* Retrieve Organization: GET /api/organizations/{id}/

* Update Organization: PUT /api/organizations/{id}/

* Partial Update Organization: PATCH /api/organizations/{id}/

* Delete Organization: DELETE /api/organizations/{id}/

Role,

* List Roles: GET /api/roles/

* Create Role: POST /api/roles/

* Retrieve Role: GET /api/roles/{id}/

* Update Role: PUT /api/roles/{id}/

* Partial Update Role: PATCH /api/roles/{id}/

* Delete Role: DELETE /api/roles/{id}/

User,

* List Users: GET /api/users/

* Create User: POST /api/users/

* Retrieve User: GET /api/users/{id}/

* Update User: PUT /api/users/{id}/

* Partial Update User: PATCH /api/users/{id}/

* Delete User: DELETE /api/users/{id}/


Permissions:

* The project uses custom permission classes to handle role-based access control. Below are the permission rules:

OrganizationViewSet:

* Create: IsSuperAdminOrAdmin

* Update/Partial Update: IsSuperAdmin or IsAdmin

* Delete: IsSuperAdmin or IsAdmin


RoleViewSet:

* Create: IsSuperAdminOrAdmin

* Update/Partial Update: IsSuperAdmin or IsAdmin

* Delete: IsSuperAdmin or IsAdmin

UserViewSet:

* Create: IsSuperAdminOrAdmin

* Update/Partial Update: IsSuperAdmin, IsAdmin, or IsManager

* Delete: IsSuperAdmin or IsAdmin

* List: IsSuperAdmin, IsAdmin, or IsManager

* Retrieve: IsSuperAdmin, IsAdmin, IsManager, or IsMember

Models:

Organization,

Fields:
name: Name of the organization
description: Description of the organization
created_at: Timestamp when the organization was created

Role,

Fields:
name: Name of the role
description: Description of the role
organization: Foreign key to the organization

User,

Fields:
email: Unique email address
organization: Foreign key to the organization
roles: Many-to-many relationship with roles

Custom Permissions:

Permission Classes:

* IsSuperAdmin: Grants access to superusers.

* IsAdmin: Grants access to admin users.

* IsManager: Grants access to users with the "Manager" role.

* IsMember: Grants access to authenticated users.

* IsSuperAdminOrAdmin: Grants access to superusers or admin users.

Serializer Details:

OrganizationSerializer:

* Fields: All fields in the Organization model.

* RoleSerializer

* Fields: All fields in the Role model.

UserSerializer:

* Fields: All fields in the User model.
