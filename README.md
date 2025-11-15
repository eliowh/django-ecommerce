# Django E-commerce Application

This is a Django-based e-commerce application that allows users to browse products, manage a shopping cart, and process orders. 

## Project Structure

```
django-ecommerce/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── ecommerce/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   ├── cart/
│   └── payments/
├── templates/
├── static/
├── media/
└── docs/
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd django-ecommerce
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your environment variables, such as:
   ```
   SECRET_KEY='your-secret-key'
   DEBUG=True
   DATABASE_URL='your-database-url'
   ```

5. **Run migrations:**
   ```
   python manage.py migrate
   ```

6. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage Guidelines

- Access the application at `http://127.0.0.1:8000/`.
- Admin panel can be accessed at `http://127.0.0.1:8000/admin/`.

## Features

- User registration and authentication
- Product listing and detail views
- Shopping cart functionality
- Order processing and payment integration

## Documentation

Refer to the `docs/` directory for detailed architecture and API documentation.