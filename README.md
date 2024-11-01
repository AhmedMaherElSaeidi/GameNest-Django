# GameNest

**GameNest** is a gaming hub platform developed as a graduation project during a one-month IT internship. It allows users to explore a variety of games, add them to their cart, manage orders, and complete purchases. Admins can manage game listings, categories, and user orders.

## Features

### User Features
- **Browse Games**: View available games organized by categories.
- **Cart Management**: Add games to your cart and manage them before purchase.
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
    git clone https://github.com/yourusername/gamenest.git
    cd gamenest
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL Database**:
    - Ensure PostgreSQL is installed and running on your system.
    - Create a PostgreSQL database named `gamenest`:
      ```sql
      CREATE DATABASE gamenest;
      ```
    - Update your database configuration in the `settings.py` file:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'gamenest',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',
              'PORT': '5432',
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

7. **Load Initial Data (Optional)**:
    If you have a fixture file to load sample data, run:
    ```bash
    python manage.py loaddata <fixture_file.json>
    ```

8. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

9. **Access the Platform**:
    - Open a web browser and go to `http://127.0.0.1:8000` to view the application.
    - Use the superuser credentials to log in to the admin panel at `http://127.0.0.1:8000/admin`.

## Usage

- **Explore Games**: Browse through the homepage to see the list of available games and categories.
- **Add to Cart**: Click on any game to add it to your cart, then proceed to checkout to complete your purchase.
- **Admin Controls**: Admins can log in to access options to add, edit, or remove games and categories, as well as manage user orders.

