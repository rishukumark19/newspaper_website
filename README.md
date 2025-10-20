--- /dev/null
+++ b/home/siri/projects/newspaper_website/README.md
@@ -0,0 +1,91 @@
+# Django Newspaper Website
+
+A full-featured newspaper and blogging platform built with Django. This project was developed as a comprehensive exercise to learn and implement core concepts of web development, from backend logic and database management to frontend presentation and production deployment.
+
+## Project Overview
+
+This application provides a complete content management system for a newspaper or blog. It includes robust user authentication, article creation and management, and a commenting system, all wrapped in a clean, responsive interface. The project is configured for seamless deployment on Vercel.
+
+## Key Features
+
+*   **User Authentication**: Secure user registration, login, logout, and password management flows.
+*   **Article CRUD**: Authenticated users can Create, Read, Update, and Delete articles.
+*   **Permissions**: Users can only edit or delete their own articles, ensuring content integrity.
+*   **Commenting System**: Logged-in users can post comments on articles.
+*   **Admin Panel**: A customized Django admin panel for easy management of articles and comments.
+*   **Responsive Design**: A clean and modern UI built with Bootstrap 5 that works on all screen sizes.
+*   **Environment-based Settings**: Securely manages configuration for development and production using `django-environ`.
+
+## My Learning Journey
+
+Building this project was a fantastic opportunity to deepen my understanding of the Django framework and modern web development practices. Key areas of learning included:
+
+- **Class-Based Views (CBVs)**: Explored a wide range of CBVs, from simple `ListView` and `DetailView` to more complex `FormView` and `SingleObjectMixin` combinations for handling GET and POST requests within the same URL.
+- **User Authentication and Authorization**: Implemented Django's built-in authentication system and extended it with custom user models and `UserPassesTestMixin` for object-level permissions.
+- **Database Modeling**: Designed and managed database schemas with Django's ORM, establishing relationships between Articles, Users, and Comments.
+- **Form Handling**: Utilized `ModelForm` for creating and validating user-submitted data for both articles and comments.
+- **Static File Management**: Configured `Whitenoise` to efficiently serve static files in a production environment.
+- **Deployment**: Gained hands-on experience deploying a Django application to a modern cloud platform (Vercel), including the creation of build scripts and serverless function configurations.
+
+## Tech Stack
+
+| Category      | Technology                                                              |
+|---------------|-------------------------------------------------------------------------|
+| **Backend**   | Python, Django                                                          |
+| **Frontend**  | HTML, Bootstrap 5                                                       |
| **Database**  | PostgreSQL (configured via `dj-database-url`)                           |
+| **Deployment**| Vercel, Gunicorn (via Vercel's Python runtime), Whitenoise              |
+| **Tooling**   | `django-environ` for configuration, `crispy-forms` for template rendering |
+
+## Local Development Setup
+
+To run this project on your local machine, follow these steps:
+
+1.  **Clone the repository:**
+    ```bash
+    git clone <your-repository-url>
+    cd newspaper_website
+    ```
+
+2.  **Create and activate a virtual environment:**
+    ```bash
+    python3 -m venv .venv
+    source .venv/bin/activate
+    # On Windows, use: .venv\Scripts\activate
+    ```
+
+3.  **Install dependencies:**
+    ```bash
+    pip install -r requirements.txt
+    ```
+
+4.  **Set up environment variables:**
+    Create a `.env` file in the project root. Add the following, replacing the values as needed:
+    ```
+    SECRET_KEY='your-super-secret-key'
+    DATABASE_URL='postgres://user:password@host:port/dbname'
+    DEBUG=True
+    ```
+    *For a simple local setup, you can use SQLite:*
+    `DATABASE_URL='sqlite:///db.sqlite3'`
+
+5.  **Run database migrations:**
+    ```bash
+    python manage.py migrate
+    ```
+
+6.  **Create a superuser:**
+    ```bash
+    python manage.py createsuperuser
+    ```
+
+7.  **Run the development server:**
+    ```bash
+    python manage.py runserver
+    ```
+    The application will be available at `http://127.0.0.1:8000`.
+
+## Deployment
+
+This project is configured for deployment on **Vercel**. The `vercel.json` file defines the build process, which uses the `@vercel/python` runtime to create a serverless function from the `django_project/wsgi.py` file. The `build.sh` script handles dependency installation, static file collection, and database migrations during the deployment pipeline.

