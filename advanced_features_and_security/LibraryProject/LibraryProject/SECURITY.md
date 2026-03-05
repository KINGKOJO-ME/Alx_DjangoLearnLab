# Django Security Implementation

This project implements several Django security best practices.

## Secure Settings

The following settings were configured in settings.py:

- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = 'DENY'
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True

These settings protect against XSS, clickjacking, and session hijacking.

## CSRF Protection

All forms include the Django template tag:

{% csrf_token %}

This prevents Cross-Site Request Forgery attacks.

## SQL Injection Prevention

Views use Django ORM queries rather than raw SQL.

Example:

Book.objects.all()

Django automatically escapes unsafe input.

## Content Security Policy

A Content Security Policy (CSP) was configured to restrict external content sources.

Only trusted sources are allowed to load scripts, styles, and images.