# Django Web and REST Framework

Learning projects and examples built while studying Django and Django REST Framework.
The repository is organized into progressive parts, from a basic Django project to
HTML-based employee management and REST API examples.

## Repository structure

```text
.
├── Notes/
│   └── Django & DRF with Rattan - Course Notes.pdf
├── part_1_code/
│   └── learning/                 # Basic Django project
└── part_2_3_code/
    ├── django_rest_framework/    # Django REST Framework examples
    └── employees/                # Employee management web application
```

Each application has its own `manage.py`, database, and virtual-environment
directory. Run commands from the directory containing the project you want to
use.

## Requirements

- Python 3.12 or newer
- Django
- Django REST Framework
- django-filter
- Pillow (required for employee image uploads)

The `requirements.txt` files contain the captured Python environments for the
two projects in `part_2_3_code`. They include additional learning and notebook
dependencies.

## Setup

Create and activate a virtual environment for the project you want to run:

```powershell
cd part_2_3_code\django_rest_framework
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install djangorestframework
```

For the employee project, use the equivalent commands:

```powershell
cd ..\employees
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install djangorestframework
```

The explicit `djangorestframework` installation is included because the
existing requirements files do not list that package, although the REST project
imports it.

## Running the projects

### Basic Django project

```powershell
cd part_1_code
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/admin/> after creating an administrator with
`python manage.py createsuperuser`.

### Django REST Framework examples

```powershell
cd part_2_3_code\django_rest_framework
python manage.py migrate
python manage.py runserver
```

Available route groups include:

- `/admin/` — Django administration
- `/students/` — student views
- `/api/v1/` — REST API routes, including the employee viewset

### Employee management application

```powershell
cd part_2_3_code\employees
python manage.py migrate
python manage.py runserver
```

The application provides employee pages, authentication routes, image uploads,
and an admin interface. In development, uploaded media is served from the
configured media directory.

## Development notes

- The projects use SQLite for local development.
- Run `python manage.py test` from the relevant project directory to execute
  its Django tests.
- Virtual environments named `venv` are ignored at every directory level by
  [`.gitignore`](.gitignore).
- Do not use the included development settings and secret keys in production.
  Move secrets to environment variables and set `DEBUG = False` before
  deployment.

## License

No license has been specified for this repository.
