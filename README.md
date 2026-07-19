<div align="center">

# 🚀 Blog App

### A Modern, Secure & High-Performance Blog Application Built with Pure Django

<img src="blog/static/images/logo.png" width="180">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.0.6-darkgreen?style=for-the-badge&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue?style=for-the-badge&logo=postgresql)
![SQLite](https://img.shields.io/badge/SQLite-Supported-lightgrey?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

Pure Django • Clean Architecture • Secure • Responsive • Production Ready

</div>

---

# 📖 About

Blog App is a fully functional blogging platform developed entirely with Pure Django, following clean coding principles and Django best practices.

The project demonstrates how to build a scalable blog without relying on external frontend frameworks or unnecessary third-party packages.

It focuses on:

- Clean Architecture
- Security
- Performance
- Maintainability
- Reusable Components
- Django Best Practices

---

# ✨ Features

## 📝 Blog

- Create, Read, Update & Delete Posts (CRUD)
- Beautiful Blog List
- Blog Detail Page
- Responsive Design
- Clean UI
- Pagination
- SEO Friendly URLs
- Optimized Database Queries
- Publish Date Management
- Draft & Published Posts
- Rich Admin Management

---

## 👤 Authentication

- User Registration
- Login
- Logout
- Password Validation
- Django Authentication System
- Permission Based Access
- Protected Views

---

## ⚡ Performance

- ORM Query Optimization
- Efficient Database Relations
- Lightweight Templates
- Fast Page Rendering
- Static File Optimization
- Optimized SQL Queries

---

## 🔐 Security

- CSRF Protection
- XSS Protection
- SQL Injection Protection
- Django Security Middleware
- Secure Form Validation
- Authentication Required Views
- Safe Template Rendering
- Input Sanitization
- Error Handling

---

## 🎨 Frontend

- Pure HTML
- Pure CSS
- Vanilla JavaScript
- Responsive Layout
- Reusable Components
- Template Inheritance
- Static File Management

---

## ⚙ Django Features

- Class-Based Views (CBV)
- Custom Model Managers
- Custom Template Filters
- Middleware
- Django ORM
- Form Validation
- Admin Customization
- Static & Media Handling
- URL Routing
- Context Processors
- Template Inheritance
- Reusable Apps
- Migration System

---

# 🛠 Tech Stack

| Technology | Version |
|------------|---------|
| Python | 3.14 |
| Django | 6.0.6 |
| HTML5 | Latest |
| CSS3 | Latest |
| JavaScript | ES6 |
| SQLite | Supported |
| PostgreSQL | Supported |
| Django ORM | ✔ |
| ASGI | ✔ |
| WSGI | ✔ |

---

# 📦 Installed Packages


asgiref==3.11.1
Django==6.0.6
django-jalali==7.4.0
jalali_core==1.0.0
jdatetime==6.0.1
sqlparse==0.5.5


---

# 📂 Project Structure


BlogApp
│
├── blog/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── tahaFirstapp/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
└── db.sqlite3


---

# ⚙ Installation

## 1. Clone Repository

bash
git clone https://github.com/YourUsername/blog-app.git


---

## 2. Go to Project

bash
cd blog-app


---

## 3. Create Virtual Environment

Windows

bash
python -m venv venv


Linux / macOS

bash
python3 -m venv venv


---

## 4. Activate Virtual Environment

Windows

bash
venv\Scripts\activate


Linux / macOS

bash
source venv/bin/activate


---

## 5. Install Dependencies

bash
pip install -r requirements.txt


---

## 6. Apply Migrations

bash
python manage.py migrate


---

## 7. Create Superuser

bash
python manage.py createsuperuser


---

## 8. Run Development Server

bash
python manage.py runserver


Open your browser:


http://127.0.0.1:8000/


Admin Panel:


http://127.0.0.1:8000/admin/


---

# 📚 Learning Concepts
This project covers many important Django concepts:

- Django Models
- Django ORM
- Class-Based Views
- URL Routing
- Template Inheritance
- Template Tags
- Template Filters
- Model Managers
- Authentication
- Authorization
- Forms
- Middleware
- Admin Customization
- Pagination
- Static Files
- Media Files
- Query Optimization
- Security Best Practices

---

# 🎯 Future Improvements

- Comment System
- Like & Bookmark
- Search
- Categories
- Tags
- Rich Text Editor
- User Profiles
- REST API
- Email Verification
- Password Reset
- Dark Mode
- CKEditor
- Docker Support
- Redis Cache
- Celery Background Tasks
- Image Upload
- Unit Tests
- CI/CD
- Deployment Guide

---

# 🤝 Contributing

Contributions, issues and feature requests are welcome.

Feel free to fork the repository and submit a Pull Request.

---

# 👨‍💻 Developer

Taha Saeidi

Backend Developer

Python • Django • PostgreSQL • REST API

GitHub:

https://github.com/YourUsername


---

<div align="center">

### ⭐ If you like this project, don't forget to give it a Star ⭐

Made with ❤️ using Django

</div>
# ===========================
# Python
# ===========================
pycache/
*.py[cod]
*$py.class

# ===========================
# Virtual Environment
# ===========================
venv/
env/
ENV/
.venv/

# ===========================
# Django
# ===========================
db.sqlite3
*.sqlite3

media/

staticfiles/

# ===========================
# Environment Variables
# ===========================
.env
.env.*

# ===========================
# VS Code
# ===========================
.vscode/

# ===========================
# PyCharm
# ===========================
.idea/

# ===========================
# macOS
# ===========================
.DS_Store

# ===========================
# Windows
# ===========================
Thumbs.db
Desktop.ini

# ===========================
# Logs
# ===========================
*.log

# ===========================
# Coverage
# ===========================
.coverage
htmlcov/
.pytest_cache/

# ===========================
# Mypy
# ===========================
.mypy_cache/

# ===========================
# Ruff
# ===========================
.ruff_cache/

# ===========================
# Distribution
# ===========================
build/
dist/
*.egg-info/

# ===========================
# Jupyter
# ===========================
.ipynb_checkpoints/

# ===========================
# Cache
# ===========================
.cache/
