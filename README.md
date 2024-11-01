# GameNest

**GameNest** is a gaming hub platform developed as a graduation project during a one-month internship. It allows users to explore a variety of games, add them to their cart, and manage orders. Admins can manage game listings, categories, and user orders.

## Features

### User Features
- **Browse Games**: View available games organized by categories.
- **Order Management**: View all ordered games in a personal order history.

### Admin Features
- **Game Management**: Create, edit, and delete games and categories.
- **Order Approval**: Review and accept or refuse user orders.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Jinja templates
- **Database**: PostgreSQL (using Psycopg2 as the ORM)

## Setup and Installation

Follow these steps to set up and run the *GameNest* project on your local machine:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AhmedMaherElSaeidi/GameNest-Django.git
    cd GameNest-Django
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv .venv
    .venv\scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL Database**:
    - Ensure PostgreSQL is installed and running on your system.
    - Create a PostgreSQL database named `gamenest_db`:
      ```sql
      CREATE DATABASE gamenest_db;
      ```
    - Update your database configuration in the `settings.py` file:
      ```python
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "gamenest_db",
                "USER": "user",
                "PASSWORD": "****",
                "HOST": "127.0.0.1",
                "PORT": "5432",
            }
        }
      ```

5. **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (for Admin Access)**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the Development Server**:
    ```bash
    python .\manage.py runserver
    ```

9. **Access the Platform**:
    - Open a web browser and go to `http://127.0.0.1:8000` to view the application.
    - Use the superuser credentials to log in to the admin panel at `http://127.0.0.1:8000/admin`.

