# My First Django Project

This is the first Django project created while learning Django.
This project contains a `polls` app that manages articles and memos.

## Features

- **Polls App**: Manages `Article` and `Memo` models.
- **Views**:
    - Displays a list of memos.
    - Shows statistics about memos.
    - Includes some simple HTML pages for practice.
- **Admin**: You can manage the models through the Django admin interface.

## Models

### Article
- `title`: CharField
- `content`: TextField
- `created_at`: DateField
- `updated_at`: DateField

### Memo
- `title`: CharField
- `content`: TextField
- `is_important`: BooleanField
- `created_at`: DateTimeField

## URLs

- `/polls/`: Index page that displays a list of memos.
- `/polls/hello/`: A simple "Hello World" page.
- `/polls/good/`: A page with some CSS styling.
- `/polls/memo/`: A page that lists memos, separating important ones.
- `/polls/memo/stats/`: A page that shows statistics about the memos.
- `/admin/`: The Django admin interface.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install Django
    ```

2.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

3.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.