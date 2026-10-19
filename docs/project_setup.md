# Project Setup Instructions

This guide will walk you through the process of setting up the **Great Minds** project on your local machine for development and testing purposes.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.10+** (Check with `python --version`)
- **PostgreSQL** (Check with `psql --version`)
- **Git** (Check with `git --version`)

---

## Setup Guide

### Step 1: Clone the Repository

First, clone the project from GitHub and navigate into the project directory:

```bash
git clone https://github.com/IvanovTech24/Great-Minds.git
cd Great-Minds
```

### Step 2: Configure Environment Variables

It is highly recommended to use a virtual environment to isolate the project dependencies.

**On Windows:**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Note:** If you encounter a PowerShell execution policy error, run the following command first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

Once the virtual environment is activated, install all required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

Ensure PostgreSQL is running and set up your database using the credentials provided in the .env file.

Next, run the following commands to apply database migrations:

```sql
CREATE DATABASE great_minds_db;
CREATE USER great_minds_user WITH PASSWORD 'your_secure_password';
ALTER ROLE great_minds_user SET client_encoding TO 'utf8';
ALTER ROLE great_minds_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE great_minds_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE great_minds_db TO great_minds_user;
```

### Step 5: Environment Variables

The project uses a `.env` file to keep sensitive data (like database credentials and the secret key) out of version control.

In the root directory of the project, create a new file named `.env`.

You can use the provided `.env.example` as a template. Copy its contents into your `.env` file and fill in your actual credentials:

```env
# Django Settings
SECRET_KEY=your-django-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database Credentials
DB_NAME=great_minds_db
DB_USER=great_minds_user
DB_PASS=your_secure_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

> **Note:** Make sure `DB_PASS` matches the password you set in Step 4.

### Step 6: Apply Database Migrations

Now that the database is configured and connected, apply the initial Django migrations to create the necessary tables:

```bash
python manage.py migrate
```

### Step 7: Create a Superuser (Admin)

To access the Django Admin panel and start adding data, you need to create an administrator account:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email, and password.

### Step 8: Run the Development Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

The application should now be running!

- **Main Website:** Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
- **Admin Panel:** Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.

---

## Troubleshooting

### Database Connection Error

Double-check your `.env` file. Ensure the `DB_USER`, `DB_PASS`, and `DB_NAME` exactly match what you created in PostgreSQL.

### Module Not Found (e.g., psycopg2)

Ensure your virtual environment is activated and run the following command again:

```bash
pip install -r requirements.txt
```

### Port 8000 Already in Use

You can run the server on a different port using:

```bash
python manage.py runserver 8080
```