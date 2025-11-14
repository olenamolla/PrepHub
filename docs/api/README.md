# PrepHub API

This document describes the current Problem endpoints exposed by the Django REST Framework API.

- Base URL (local dev): `http://127.0.0.1:8000/api/`
- Authentication: None (MVP, JWT planned)
- CORS: Allowed for `http://localhost:3000` and `http://127.0.0.1:3000`
- Frameworks: Django + DRF

## Problem Endpoints

### List Problems
- Method: `GET`
- URL: `/problems/`
- Query params: none (pagination and ordering planned later)
- Response 200 (application/json):
```json
[
  {
    "id": 1,
    "title": "Two Sum",
    "difficulty": "Easy",
    "topic": "Arrays",
    "notes": "it was easy to solve such a problem",
    "solved_date": "2025-11-07T22:30:07Z"
  }
]
```

### Create Problem
- Method: `POST`
- URL: `/problems/`
- Headers: `Content-Type: application/json`
- Body (example):
```json
{
  "title": "Binary Search",
  "difficulty": "Medium",
  "topic": "Arrays",
  "notes": "Watch for mid calculation and bounds",
  "solved_date": "2025-11-14T10:30:00Z"
}
```
- Response 201 (application/json):
```json
{
  "id": 3,
  "title": "Binary Search",
  "difficulty": "Medium",
  "topic": "Arrays",
  "notes": "Watch for mid calculation and bounds",
  "solved_date": "2025-11-14T10:30:00Z"
}
```

### Error Responses
- Response 400 (validation errors):
```json
{
  "title": ["This field is required."],
  "difficulty": ["This field is required."],
  "topic": ["This field is required."]
}
```

## Notes
- Browsable API available at `/api/` if DRF is installed and DEBUG is on.
- Root path `/` is not routed and returns 404; available routes start with `/api/` and `/admin/`.
- More endpoints (retrieve/update/delete) are provided automatically by DRF `ModelViewSet` at `/api/problems/{id}/` and follow the usual HTTP verbs.

## References
- Django REST Framework: https://www.django-rest-framework.org/
- DRF Quickstart (ViewSets & Routers): https://www.django-rest-framework.org/tutorial/quickstart/
- django-cors-headers: https://github.com/adamchainz/django-cors-headers
