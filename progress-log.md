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

---

**Date:** November 9, 2025

**Summary:**
- Installed Django REST Framework (DRF) and added it to `INSTALLED_APPS` in `settings.py`
- Created `serializers.py` in the `problems` app and implemented `ProblemSerializer` using DRF’s `ModelSerializer`
- Committed and pushed changes to Git

**What I Learned:**
- Why DRF is used for building APIs in Django
- How serializers work and why we subclass `ModelSerializer`
- The purpose of the `Meta` subclass and the meaning of `model = Problem`
- How to control which fields are exposed in the API

**Next Steps:**
1. Create the first API endpoint for the Problem model using DRF ViewSets
2. Set up routing in `urls.py`
3. Add basic API tests
4. Configure CORS for frontend integration

---

**Date:** November 11, 2025

**Summary:**
- Implemented first API endpoint with `ProblemViewSet (ModelViewSet)`
- Registered DRF `DefaultRouter` and wired `/api/problems/` routes in `prephub/urls.py`
- Verified the endpoint via the browsable API (GET `/api/problems/` returns JSON)
- Added learning notes in `mds/editorial-notes.md` (serializer → viewset → router flow)
- Committed and pushed changes

**What I Learned (programmer terms):**
- Routing: `DefaultRouter()` instance generates URL patterns; `register('problems', ProblemViewSet)` binds prefix → class; `include(router.urls)` mounts under `/api/`
- View layer: `ModelViewSet` provides CRUD actions; configure `queryset` and `serializer_class`
- Data flow: Request → URLConf → Router → ViewSet action → QuerySet/ORM → Serializer → JSON Response

**Next Steps:**
1. Add API tests (DRF APIClient):
	- GET `/api/problems/` returns 200 and a list
	- POST valid payload returns 201 and persists
	- POST invalid payload returns 400 with errors
2. Configure CORS for upcoming frontend work (`django-cors-headers`)
3. Optional: add ordering by `solved_date` and test retrieve/update/delete
4. Document endpoints (README or OpenAPI) and keep progress-log updated
