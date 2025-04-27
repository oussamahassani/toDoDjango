# ToDoDjango

This is a simple To-Do list application built with Django. It allows users to register, log in, and manage their daily tasks. Users can add, edit, and delete tasks, and the app supports basic user authentication.

## Features

- User registration and login.
- Add, edit, and delete tasks.
- View a list of all tasks.
- Mark tasks as completed.
- Simple and user-friendly interface.

## Installation

### Prerequisites

Ensure that you have the following installed:

- Python 3.x
- Django
- pip (Python package manager)

### Steps to set up the project:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/oussamahassani/toDoDjango.git
    ```

2. Navigate into the project directory:

    ```bash
    cd toDoDjango
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
    venv\Scripts\activate     # For Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:

    ```bash
    python manage.py migrate
    ```

6. Create a superuser to access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your browser and navigate to `http://127.0.0.1:8000/` to see the app in action.

## Usage

- **Registration**: To use the app, register an account by clicking on "Register" from the home page.
- **Login**: After registering, log in using your credentials.
- **Manage Tasks**: Once logged in, you can add new tasks, edit existing ones, and mark them as complete.

## Project Structure

