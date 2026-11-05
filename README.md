# To-Do List Web Application Using Django

An interactive, responsive To-Do List web application developed using **Django**, **HTML5**, and **CSS3** for the Semester 3 Web Development II assignment. The application enables users to manage their daily tasks through an intuitive user interface with complete CRUD (Create, Read, Update, Delete) functionality.

**Author**: Sumati Sen  
**Repository**: [https://github.com/sumatisen/to_do_list_assignment](https://github.com/sumatisen/to_do_list_assignment)

---

## Objective & Features

The objective of this assignment is to build a full-featured task management web application adhering to Django's MTV (Model-Template-View) design pattern.

### Functional Requirements

1. **Home Page / Dashboard (`/`)**:
   - Clean, modern navigation bar with application title **Todo App** and a direct **Add Task** action button.
   - Central table displaying all tasks with columns: `Title`, `Description`, `Done`, `Created`, and `Actions`.
2. **Add Task (`/add_task/`)**:
   - Dedicated page with a form accepting a task `Title` and `Description`.
   - Action buttons: **Save** (primary) and **Cancel** (returns to dashboard).
3. **Display Tasks**:
   - Lists tasks dynamically rendered via Django templates.
   - Formatted creation timestamp (`YYYY-MM-DD HH:MM`).
4. **Update Task (`/edit_task/<id>/`)**:
   - Edit existing task details (title and description) and update completion status via checkbox.
5. **Mark as Completed (`/toggle_task/<id>/`)**:
   - Interactive checkbox directly in the dashboard table allowing one-click status toggle between completed and pending.
6. **Delete Task (`/delete_task/<id>/`)**:
   - Immediate task removal with browser confirmation prompt.
7. **Task Status Distinction**:
   - Completed tasks display a subtle green background highlight (`.task-done`), struck-through title text, and green checkbox state.
8. **Empty State**:
   - Clean notification banner stating `"No tasks yet."` displayed when the task list is empty.

---

## Technical Stack & Architecture

- **Backend**: Python 3, Django 6.1 (MTV Architectural Pattern)
- **Database**: SQLite3 (managed via Django ORM and migrations)
- **Frontend**: HTML5, CSS3 (Modular design, responsive typography, custom design system)
- **Security**: Built-in Django CSRF tokens applied to all form submissions

---

## Project Structure

```text
to_do_list_project/
├── manage.py                          # Django management CLI utility
├── db.sqlite3                         # SQLite database with initial sample data
├── README.md                          # Documentation and setup instructions
├── to_do_list_project/                # Project configuration package
│   ├── __init__.py
│   ├── settings.py                   # App settings, static configuration, timezone
│   ├── urls.py                       # Root URL dispatcher
│   ├── asgi.py                       # ASGI configuration
│   └── wsgi.py                       # WSGI deployment configuration
├── to_do_list_app/                    # Core Django application
│   ├── __init__.py
│   ├── admin.py                      # Django Admin site registration
│   ├── apps.py                       # Application configuration
│   ├── forms.py                      # Django ModelForms (TaskForm, TaskEditForm)
│   ├── models.py                     # Task model (title, description, done, created_at)
│   ├── tests.py                      # Automated test suite (15 unit test cases)
│   ├── urls.py                       # Application URL routing
│   ├── views.py                      # View controller functions (CRUD + Toggle)
│   └── migrations/                   # Database migrations
│       ├── 0001_initial.py
│       └── __init__.py
├── templates/                         # Django HTML templates
│   ├── base.html                     # Main layout template
│   ├── navbar.html                   # Navigation header component
│   ├── home.html                     # Task list dashboard
│   ├── add_task.html                 # Task creation view
│   └── edit_task.html                # Task update view
└── static/                            # Static CSS assets
    ├── home.css                      # Static asset alias
    ├── add_task.css                  # Static asset alias
    ├── edit_task.css                 # Static asset alias
    └── css/
        ├── style.css                 # Master application design system
        ├── home.css                  # Dashboard styling
        ├── add_task.css              # Add task styling
        └── edit_task.css             # Edit task styling
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sumatisen/to_do_list_assignment.git
cd to_do_list_assignment
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Apply Database Migrations
```bash
python3 manage.py migrate
```

### 5. Start the Development Server
```bash
python3 manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

---

## Running Automated Tests

Run the Django automated test suite covering models, views, forms, and status toggles:

```bash
python3 manage.py test
```

All 15 test cases execute and verify CRUD operations, redirects, form validation, and empty state rendering.
