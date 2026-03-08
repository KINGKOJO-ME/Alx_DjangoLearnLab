# Social Media API

## Setup

1. Clone repository
2. Install dependencies

pip install django djangorestframework pillow

3. Run migrations

python manage.py migrate

4. Start server

python manage.py runserver

## API Endpoints

Register
POST /api/accounts/register/

Login
POST /api/accounts/login/

Profile
GET /api/accounts/profile/

Authentication uses Token Authentication.