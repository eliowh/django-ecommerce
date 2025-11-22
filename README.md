# Django E-commerce Application

**IT 403 WMAD - Elective 5 (WST 3)**  
**Bulacan State University**  
**College of Information and Communications Technology**

This is a comprehensive Django-based e-commerce application that provides a complete online shopping platform with user management, product catalog, shopping cart functionality, and order processing capabilities. 

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

### Core Functionality
- **User Management**: Registration, authentication, and profile management
- **Product Catalog**: Categorized product listing with search and filtering
- **Shopping Cart**: Add, modify, and manage cart items
- **Order Processing**: Complete order workflow with address management
- **Payment Integration**: Secure payment processing with Stripe
- **Admin Panel**: Comprehensive administrative tools

### Technical Features
- **RESTful API**: Django REST Framework implementation
- **Responsive Design**: Mobile-friendly user interface
- **Security**: Secure authentication and data protection
- **Database**: Optimized database schema with proper relationships
- **Testing**: Comprehensive test coverage

## Quick Start

### Sample Data Population
After completing the installation steps above, populate the database with sample data:

```bash
python manage.py populate_sample_data
```

This will create:
- Sample user accounts (username: john_doe, jane_smith, mike_wilson, admin)
- Product categories (Electronics, Clothing, Books, etc.)
- Sample products with realistic data
- Shopping carts and orders for demonstration

### Default Login Credentials
- **Admin User**: username: `admin`, password: `admin123`
- **Customer**: username: `john_doe`, password: `testpass123`

## Project Deliverables (IT 403)

### ✅ Completed Deliverables
1. **System Proposal** - Available in `docs/SYSTEM_PROPOSAL.md`
2. **Django Project Folder** - Complete source code with working functionality
3. **Database (SQLite)** - Includes migrations and sample data
4. **Documentation** - Comprehensive project documentation in `docs/`
5. **ERD (Entity Relationship Diagram)** - Mermaid diagram in documentation

### 📁 Project Structure for Submission
```
django-ecommerce/
├── docs/
│   ├── SYSTEM_PROPOSAL.md     # System proposal document
│   ├── PROJECT_DOCUMENTATION.md  # Complete project documentation
│   ├── api.md                 # API documentation
│   └── architecture.md        # System architecture
├── apps/                      # Django applications
├── templates/                 # HTML templates
├── static/                    # Static files (CSS, JS, images)
├── db.sqlite3                # Database with sample data
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Documentation

Refer to the `docs/` directory for detailed documentation:
- **System Proposal**: `docs/SYSTEM_PROPOSAL.md`
- **Project Documentation**: `docs/PROJECT_DOCUMENTATION.md`
- **API Documentation**: `docs/api.md`
- **Architecture Guide**: `docs/architecture.md`

## Academic Information

**Course**: IT 403 WMAD - Elective 5 (WST 3)  
**Institution**: Bulacan State University  
**College**: College of Information and Communications Technology  
**Academic Year**: 2025