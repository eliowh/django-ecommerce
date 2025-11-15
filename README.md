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
   ```bash
   git clone <repository-url>
   cd django-ecommerce
   ```

2. **Create a virtual environment and activate it**

   POSIX (macOS / Linux / Git Bash):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows (PowerShell) — recommended for Windows users:
   ```powershell
   python -m venv venv
   # allow running local scripts for this session (temporary)
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
   # activate the venv (use .\venv or .\.venv depending on folder name)
   . .\venv\Scripts\Activate.ps1
   ```

   Windows (cmd.exe):
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```

3. **Install dependencies (use python -m pip to avoid interpreter mismatch)**

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

   Note: this project uses `python-dotenv` to load `.env` variables. If you see an error about `dotenv`, install it explicitly or update `requirements.txt`:
   ```powershell
   python -m pip install python-dotenv
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root (same folder as `manage.py`). Example `.env` for local development:
   ```dotenv
   SECRET_KEY=your-very-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   # Optional: DATABASE_URL (for sqlite or other DB)
   # For sqlite (relative file):
   DATABASE_URL=sqlite:///db.sqlite3
   # For Postgres:
   # DATABASE_URL=postgres://user:password@host:5432/dbname
   ```

   Important:
   - Don't commit real secrets. Add `.env` to `.gitignore`.
   - `DEBUG` is read as a string in the settings file, so use `DEBUG=True` or `DEBUG=False` (capitalized text).

5. **Migrations**

   If this is the first time running the project locally and you or the repo changed the custom user model, run:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

   If `makemigrations` isn't necessary (migrations are in the repo), you can run just:
   ```powershell
   python manage.py migrate
   ```

6. **Create a superuser**

   ```powershell
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```powershell
   python manage.py runserver
   ```

8. **Troubleshooting / tips**

- Use `python -m pip install` so pip targets the same interpreter used to run `manage.py`.
- If you see "No module named 'dotenv'" install `python-dotenv` or add it to `requirements.txt`.
- If Django fails to import because of missing views or broken imports during `migrate`, inspect `apps/*/urls.py` and the referenced view modules — Django imports URL modules at startup and any import error blocks `manage.py` commands.
- If you use a custom `AUTH_USER_MODEL`, make sure `AUTH_USER_MODEL` is set in `ecommerce/settings.py` and the app has migrations checked into the repo, or run `makemigrations` before `migrate`.

If you want, I can update `requirements.txt` to add `python-dotenv` and open a PR with these README edits so your team has a single authoritative setup guide.

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