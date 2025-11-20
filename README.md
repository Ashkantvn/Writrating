# 🛠️ Writrating - Account & Device

## 📖 Overview

This repository contains **two Django REST Framework (DRF)** microservices:

1. **Account Service** — Handles user registration, authentication, and profile management.
2. **Device Service** — Manages device ratings and profiles, linked to authenticated users.

Both services authenticate and communicate using **JWT (RS256)** tokens. The repository includes Docker configs for local development and production-ready images.

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Quickstart — Local (venv)](#-quickstart--local-venv)
- [Quickstart — Docker (development)](#-quickstart--docker-development)
- [Running Tests](#-running-tests)
- [Environment / Configuration](#-environment--configuration)
- [JWT (RS256) Keys](#-jwt-rs256-keys)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)# 🛠️ Writrating - Account & Device

## 📖 Overview

This repository contains **two Django REST Framework (DRF)** microservices:

1. **Account Service** — Handles user registration, authentication, and profile management.
2. **Device Service** — Manages device ratings and profiles, linked to authenticated users.

Both services authenticate and communicate using **JWT (RS256)** tokens. The repository includes Docker configs for local development and production-ready images.

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Quickstart — Local (venv)](#-quickstart--local-venv)
- [Quickstart — Docker (development)](#-quickstart--docker-development)
- [Running Tests](#-running-tests)
- [JWT (RS256) Keys](#-jwt-rs256-keys)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## ⚙️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django |
| API | Django REST Framework (DRF) |
| Auth | SimpleJWT (RS256) |
| Docs | drf-spectacular |
| Config | python-decouple |
| Database | PostgreSQL |
| Linting | black, flake8 |
| Testing | pytest, pytest-django |
| Containerization | Docker |

---

## ⚡ Quickstart — Local (venv)

Follow these steps to run a single service locally. Example uses the `account_service` — repeat similarly for `devices_service`.

1. Create and activate a virtual environment, install deps:

```bash
cd account_service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables (example):

```bash
export DJANGO_SETTINGS_MODULE=account_service.settings.dev
export SECRET_KEY="replace-with-a-secret"
```

3. Run migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Repeat for `devices_service` by changing into that directory first.

---

## 🐳 Quickstart — Docker (development)

Each service provides Dockerfiles and `docker-compose` configs under `account_service/docker/` and `devices_service/docker/`.

Example (account service):

```bash
docker compose -f account_service/docker/docker-compose.dev.yml up --build
```

Example (devices service):

```bash
docker compose -f devices_service/docker/docker-compose.dev.yml up --build
```
---

## ✅ Running Tests

Run tests for a service from that service directory:

```bash
cd account_service
pytest

cd ../devices_service
pytest
```

---

## 🔐 JWT (RS256) Keys

This project uses RS256-signed JWTs. You can generate a key pair using OpenSSL:

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

Place the private key where the service can read it (e.g. `account_service/keys/private.pem`) and set `JWT_PRIVATE_KEY_PATH` / `JWT_PUBLIC_KEY_PATH` accordingly.

---

## 📄 API Documentation

Each service includes `drf-spectacular` for OpenAPI schema generation. Typical local endpoints to try (may vary by service routing):

- Schema JSON: `/api/schema/`
- Swagger UI: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`

---

## 🤝 Contributing

- Fork and open a pull request. Add tests for new features or bug fixes.

---

## 🏁 License

This project is licensed under the MIT License. See the top-level `LICENSE` file for details.

---

- [License](#-license)

---

## ⚙️ Tech Stack

| Category | Technology |
|-----------|-------------|
| Framework | Django |
| API | Django REST Framework (DRF) |
| Auth | SimpleJWT (RS256) |
| Docs | drf-spectacular |
| Config | python-decouple |
| Database | PostgreSQL |
| Linting | black, flake8 |
| Testing | pytest, pytest-django |
| Containerization | Docker |

---

## ⚡ Quickstart — Local (venv)

Follow these steps to run a single service locally. Example uses the `account_service` — repeat similarly for `devices_service`.

1. Create and activate a virtual environment, install deps:

```bash
cd account_service
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set environment variables (example):

```bash
export DJANGO_SETTINGS_MODULE=account_service.settings.dev
export SECRET_KEY="replace-with-a-secret"
```

3. Run migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Repeat for `devices_service` by changing into that directory first.

---

## 🐳 Quickstart — Docker (development)

Each service provides Dockerfiles and `docker-compose` configs under `account_service/docker/` and `devices_service/docker/`.

Example (account service):

```bash
docker compose -f account_service/docker/docker-compose.dev.yml up --build
```

Example (devices service):

```bash
docker compose -f devices_service/docker/docker-compose.dev.yml up --build
```

Use `-d` to run containers in the background and `--env-file` to pass environment variables from a file.

---

## ✅ Running Tests

Run tests for a service from that service directory:

```bash
cd account_service
pytest -q

cd ../devices_service
pytest -q
```

You can also run tests from the repository root by pointing `pytest` to a service folder:

```bash
pytest account_service -q
pytest devices_service -q
```

---

## 🔧 Environment / Configuration

The projects use a `settings/` package with `dev.py` and `prod.py`. Set `DJANGO_SETTINGS_MODULE` to the appropriate module (for example `account_service.settings.dev`).

Common environment variables used by the services (example):

- `SECRET_KEY`
- `DATABASE_URL` (or local `DATABASES` settings)
- `DEBUG` (true/false)
- `ALLOWED_HOSTS`
- `JWT_PRIVATE_KEY_PATH`
- `JWT_PUBLIC_KEY_PATH`

Create a `.env` or `.env.example` in the service directory with these variables for local development.

Example `.env.example` snippet:

```env
SECRET_KEY=replace-me
DATABASE_URL=postgres://user:pass@localhost:5432/dbname
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
JWT_PRIVATE_KEY_PATH=./keys/private.pem
JWT_PUBLIC_KEY_PATH=./keys/public.pem
```

---

## 🔐 JWT (RS256) Keys

This project uses RS256-signed JWTs. You can generate a key pair using OpenSSL:

```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

Place the private key where the service can read it (e.g. `account_service/keys/private.pem`) and set `JWT_PRIVATE_KEY_PATH` / `JWT_PUBLIC_KEY_PATH` accordingly. If you prefer, use a secrets manager or mount keys into the container at runtime.

If you’d like, I can add a small management command or startup check to validate keys exist and are readable.

---

## 📄 API Documentation

Each service includes `drf-spectacular` for OpenAPI schema generation. Typical local endpoints to try (may vary by service routing):

- Schema JSON: `/api/schema/`
- Swagger UI: `/api/schema/swagger-ui/`
- Redoc: `/api/schema/redoc/`

If routes differ, I can inspect `urls.py` in each service and update the README with exact paths.

---

## 🤝 Contributing

- Fork and open a pull request. Add tests for new features or bug fixes.
- Keep changes scoped to a single service where possible.

---

## 🏁 License

This project is licensed under the MIT License. See the top-level `LICENSE` file for details.

---

If you want, I can also:

- add example cURL / HTTPie requests for common endpoints,
- create a repository-level `.env.example` or per-service `.env.example` files,
- add a small `make` file for common tasks (run, test, lint), or
- scaffold CI to run tests on PRs.

Tell me which and I’ll add it.
