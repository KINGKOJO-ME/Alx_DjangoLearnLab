# Advanced API Project

This project demonstrates advanced Django REST Framework API development.

## Features

- Custom serializers
- Nested serializers
- CRUD operations using generic views
- Permission-based access control

## API Endpoints

| Endpoint | Method | Description |
|--------|--------|--------|
| /api/books/ | GET | List all books |
| /api/books/<id>/ | GET | Retrieve single book |
| /api/books/create/ | POST | Create book |
| /api/books/update/<id>/ | PUT | Update book |
| /api/books/delete/<id>/ | DELETE | Delete book |

## Permissions

- Read access: Public
- Write access: Authenticated users only