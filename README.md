# Django Library Management System

This is a Django-based library management system capstone project at GDSCAAstu.

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
   https://github.com/Tonetor777/Django_Library_Management_System.git
   ```

2. Navigate to the project directory:

   ```bash
   cd LibraryManagement
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies from the `Requirements.txt` file:

   ```bash
   pip install -r Requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin interface:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Log in to the Django admin interface using the credentials of the superuser created in step 6.
- Add books, manage borrowers, issue and return books, and perform other administrative tasks.
- Use the provided templates and views for borrower-facing functionalities.
- Customize the application as needed to suit your specific library management requirements.

## Contributors

contributors for this projects are `https://github.com/Rafii05k` , `https://github.com/yeabyir` and `https://github.com/Yohannes18`

