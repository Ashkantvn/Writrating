# 🛠️ Writrating - Account & Device

## 📖 Overview

This repository contains **two Django REST Framework (DRF)** microservices:

1. **Account Service** — Handles user registration, authentication, and profile management.  
2. **Device Service** — Manages device ratings, linked to authenticated users.

Both services communicate securely using **JWT (RS256)** tokens for authentication, and the entire environment is managed via **Docker**.

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

## 🔐 Authentication

Both services use **JWT (RS256)** for authentication and communication.

---

## ⚡ API Documentation

Each service includes drf-spectacular for OpenAPI schema generation.

---

## 🏁 License

This project is licensed under the MIT License.


