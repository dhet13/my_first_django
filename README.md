# My First Django Project

<<<<<<< HEAD
이 프로젝트는 Django 프레임워크 학습을 위해 만들어진 첫 번째 프로젝트입니다.

## 프로젝트 소개

Django의 기본 개념을 익히기 위한 간단한 게시글(Article) 및 메모(Memo) 관리 애플리케이션입니다. 프로젝트의 앱 이름은 `polls`로 되어 있지만, 실제 기능은 설문이 아닌 게시글과 메모 관리에 중점을 두고 있습니다. 학습 과정에서 만들어진 다양한 테스트용 뷰와 코드 주석이 포함되어 있습니다.

## 주요 기능

*   **게시글 및 메모 관리:** 간단한 텍스트 기반의 게시글과 메모를 생성하고 조회할 수 있습니다.
*   **Django Admin:** Django의 기본 관리자 페이지(`http://127.0.0.1:8000/admin/`)를 통해 데이터를 손쉽게 관리할 수 있습니다.
*   **학습용 뷰:** Django의 뷰, URL, ORM 등의 개념을 학습하기 위한 다양한 실험적인 뷰가 포함되어 있습니다.

## 프로젝트 구조

*   `config/`: 프로젝트의 전반적인 설정을 관리하는 메인 설정 디렉토리입니다. (e.g., `settings.py`, `urls.py`)
*   `polls/`: 게시글 및 메모 관리 기능이 구현된 메인 애플리케이션입니다. (e.g., `models.py`, `views.py`, `urls.py`)

## 실행 방법

1.  **Django 설치:**
=======
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
>>>>>>> d08acb3d802c4d43e517fb5a0c8d9db6c115538e
    ```bash
    pip install Django
    ```

<<<<<<< HEAD
2.  **데이터베이스 설정 (Migration):**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3.  **개발 서버 실행:**
=======
2.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

3.  **Run the development server:**
>>>>>>> d08acb3d802c4d43e517fb5a0c8d9db6c115538e
    ```bash
    python manage.py runserver
    ```

<<<<<<< HEAD
4.  **애플리케이션 접속:**
    *   메인 페이지: `http://127.0.0.1:8000/`
    *   관리자 페이지: `http://127.0.0.1:8000/admin/` (관리자 계정은 `python manage.py createsuperuser` 명령어로 생성해야 합니다.)
=======
The application will be available at `http://127.0.0.1:8000/`.
>>>>>>> d08acb3d802c4d43e517fb5a0c8d9db6c115538e
