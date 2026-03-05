# Django Permissions and Groups Implementation

This project demonstrates how to implement role-based access control in Django using custom permissions and groups.

## Custom Permissions

Custom permissions were added to the **Book model** inside:

bookshelf/models.py

The following permissions were created:

- can_view
- can_create
- can_edit
- can_delete

These permissions allow fine-grained control over which users can perform specific actions on Book objects.

Example from the model:

class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]

## Groups

Three user groups were created using Django Admin:

### Viewers
Permissions:
- can_view

### Editors
Permissions:
- can_create
- can_edit

### Admins
Permissions:
- can_view
- can_create
- can_edit
- can_delete

## Permission Enforcement

Views were protected using Django's permission system.

Example:

@permission_required('bookshelf.can_edit', raise_exception=True)

This ensures only users with the correct permission can access protected views.

## Testing

Testing was done manually by:

1. Creating test users
2. Assigning them to different groups
3. Logging in as each user
4. Verifying that access restrictions work correctly