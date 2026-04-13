# TaskFlow Backend API

## 1. Overview

TaskFlow is a backend system for managing projects and tasks with authentication, filtering, and analytics.

It allows users to:

- Register and log in
- Create and manage projects
- Create and manage tasks within projects
- Filter and paginate tasks
- View project-level analytics

### Tech Stack

- FastAPI (Python backend framework)
- PostgreSQL (database)
- SQLAlchemy (ORM)
- Alembic (database migrations)
- JWT (authentication)
- Docker & Docker Compose (containerization)
- Pytest (testing)

---

## 2. Architecture Decisions

### Layered Architecture

The project follows a modular layered architecture:

- `api/` → route definitions
- `services/` → business logic
- `models/` → database models
- `schemas/` → request/response validation
- `core/` → config, security, dependencies

This separation improves:

- Maintainability
- Testability
- Scalability

---

### Key Decisions

- Used **JWT-based authentication** for stateless sessions
- Used **SQLAlchemy ORM** for flexibility and readability
- Used **Alembic** for version-controlled database migrations
- Used **Docker Compose** to ensure consistent environment setup

---

### Tradeoffs

- Did not implement full RBAC to keep scope focused
- Used synchronous SQLAlchemy instead of async for simplicity
- Minimal error handling in some edge cases to prioritize core functionality

---

### Intentional Omiss

- No caching layer (e.g., Redis)
- No background jobs or async workers

These were omitted to keep the implementation aligned with assignment scope.

---

## 3. Running Locally

### Prerequisites

- Docker installed

---

### Steps

```bash
git clone <your-repo-url>
cd taskflow-rishav-solanki
```

---

### Start the application

```bash
docker compose up --build
```

---

### Access API

- Swagger Docs: http://localhost:8000/docs
- OpenAPI Spec: http://localhost:8000/openapi.json

---

## 4. Running Migrations

Migrations are automatically executed on container startup using:

```bash
alembic upgrade head
```

---

### Manual Migration (if needed)

```bash
docker exec -it taskflow_backend alembic upgrade head
```

---

## 5. Test Credentials

Use the following credentials to log in:

```
Email:    test@example.com
Password: password123
```

---

## 6. API Reference

### Swagger Documentation

Available at:

```
http://localhost:8000/docs
```

---

### Postman Collection

Located at:

```
/postman_collection.json
```

---

### Key Endpoints

#### Authentication

- POST `/auth/register`
- POST `/auth/login`

---

#### Projects

- GET `/projects?page=1&limit=5`
- POST `/projects`
- PATCH `/projects/{id}`
- DELETE `/projects/{id}`
- GET `/projects/{id}/stats`

---

#### Tasks

- POST `/projects/{id}/tasks`
- GET `/projects/{id}/tasks?status=todo&page=1&limit=5`
- PATCH `/tasks/{id}`
- DELETE `/tasks/{id}`

---

## 7. What I'd Do With More Time

- Implement role-based access control (RBAC)
- Add Redis caching for frequently accessed queries
- Improve test coverage (edge cases, failure scenarios)
- Introduce async database handling for better performance
- Add CI/CD pipeline for automated testing and deployment
- Improve logging and monitoring
- Add rate limiting and security enhancements

---
