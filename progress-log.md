## Progress Log

**Date:** November 6, 2025

**Summary:**
- Defined MVP core features and project scope
- Set up GitHub repository and pushed initial commit
- Created project directory structure (backend, frontend, docs)
- Added .gitignore and updated README.md
- Set up Python virtual environment in backend
- Installed Django and Django REST Framework

**Current Status:**
- Ready to initialize Django project

**Next Steps:**
1. Initialize Django project (`django-admin startproject prephub .`)
2. Configure PostgreSQL settings in Django
3. Set up basic Django app structure
4. Plan initial models for user and problem tracking

---

**Date:** November 7, 2025

**Summary:**
- Fixed Django settings after renaming project folder
- Created and registered 'problems' app
- Defined Problem model and ran migrations
- Added Problem model to admin panel and created superuser
- Logged into Django admin and explored its features

**What I Learned:**
- Difference between Django project and apps
- How migrations work and why they're needed
- How to register models with the admin panel
- What the admin panel is for
- What an API endpoint is

**Struggles Faced:**
- ModuleNotFoundError after renaming project folder
- Understanding Django's app/project structure

**Goals for Next Day:**
1. Build first API endpoint for Problem model using Django REST Framework
2. Learn about serializers and viewsets
3. Test API with tools like Postman or curl
