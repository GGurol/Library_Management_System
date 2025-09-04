# Django Library Management System

This is a Django-based library management system capstone project.

## Features

- Add, edit, and delete books.
- Issue and return books.
- View borrowed books and their status.
- Search functionality for books and borrowers.
- Ban/unban borrowers.

## Installation

Follow these steps to set up and run the Django library management system:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/GGurol/Django_Library_Management_System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Library_Management_System
   ```

3. Build the docker and build:

   ```bash
   docker compose up --build -d
   ```

4. Apply database migrations:

   ```bash
   docker compose exec web python manage.py makemigrations
   docker compose exec web python manage.py migrate
   ```

5. Create a superuser to access the admin interface:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Log in to the Django admin interface using the credentials of the superuser created in step 5.
- Add books, manage borrowers, issue and return books, and perform other administrative tasks.
- Use the provided templates and views for borrower-facing functionalities.
- Customize the application as needed to suit your specific library management requirements.

