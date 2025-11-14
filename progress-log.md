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

---

**Date:** November 12, 2025

**Summary:**
- Installed and wired `django-cors-headers` (added to `INSTALLED_APPS` and middleware)
- Configured CORS policy to allow local frontend origins (`http://localhost:3000`, `http://127.0.0.1:3000`)
- Reviewed where CORS sits in the architecture (HTTP edge/middleware) and how preflight/data requests flow
- Test suite for Problem API is passing (3 tests: list, create valid, create invalid)

**Notes:**
- Skipped the quick CORS verification commands today; configuration changes are in place and can be validated next session

**What I Learned:**
- CORS runs before view logic; the middleware adds `Access-Control-Allow-*` headers so browsers permit cross-origin calls
- Preflight (OPTIONS) vs. actual requests and how the router/viewset are only hit after CORS allows the request

**Next Steps:**
1. Verify CORS manually (preflight and GET) to confirm headers are returned
2. Update API docs or README with available endpoints and expected payloads
3. Decide next track:
   - Start frontend scaffold (React + Vite/CRA) and call `/api/problems/`
   - Or begin auth foundation (JWT) on the backend
4. Append any learnings to `mds/editorial-notes.md` as you go

---

**Date:** November 14, 2025

**Summary:**
- Verified CORS end-to-end: preflight (OPTIONS) and GET to `/api/problems/` with `Origin: http://localhost:3000` returned the expected `Access-Control-Allow-*` headers; GET returned 200 with JSON
- Added Vite dev server origins to CORS (`http://localhost:5173`, `http://127.0.0.1:5173`) so the frontend can call the API during development
- Documented current Problem endpoints in `docs/api/README.md` (list/create with sample payloads and error responses)
- Scaffolded frontend with Vite + React + TypeScript
- Installed Axios and created a reusable client in `frontend/src/services/api.ts` (with `.env` support via `VITE_API_BASE_URL`)
- Implemented the initial data fetch in `frontend/src/App.tsx` using `useEffect`/`useState` and a `Problem` TypeScript interface (UI rendering to be completed next)
- Resolved npm permissions error (`EACCES`) by resetting ownership of `~/.npm`

**What I Learned:**
- REST + SPA data flow: Browser → React (Vite dev server) → Axios → DRF (Router/ViewSet/Serializer) → JSON → UI
- CORS sits at the HTTP edge; preflight vs actual requests; why the `Origin` header matters
- Vite’s role as a fast dev server (usually on port 5173) and how it impacts CORS
- Axios vs fetch trade-offs; Axios instances simplify base URL and later JWT interceptors
- TypeScript interfaces act as contracts for API response shapes and help catch mistakes early

**Struggles Faced:**
- npm cache permission issue causing `EACCES` during scaffold (fixed with `chown` on `~/.npm`)
- DisallowedHost/404 at root: understood root (`/`) isn’t routed; use `/api/…` and add hosts as needed

**Next Steps:**
1. Finish the Problem list UI:
	- Fix endpoint typo in `App.tsx` from `/problmes/` → `/problems/`
	- Render the problems list with loading and error states (replace Vite starter content)
	- Optionally extract a small `ProblemCard` component
2. Frontend quality:
	- Add ESLint + Prettier config for the frontend and run a quick lint/format
	- Commit and push changes
3. Backend auth (next track):
	- Add JWT auth with `djangorestframework-simplejwt` (`/api/token/`, `/api/token/refresh`)
	- Protect Problem endpoints (authenticated access) and update tests/docs
4. Docs:
	- Update `docs/api/README.md` if response shapes or auth requirements change
	- Capture learnings in `mds/editorial-notes.md`
	- do a 10-minute TypeScript mini-lesson (interfaces, unions, generics) tailored to your current code before we implement ProblemCard and auth.
