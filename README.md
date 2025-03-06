# Email-Storage
## Overview
Email Storage System is a Django-based web application that allows users to store their emails securely and download them whenever needed. This project provides a simple interface to manage and retrieve stored emails efficiently.

## Features
- User authentication (signup, login, logout)
- Secure email storage
- Email upload and retrieval
- Download stored emails as files
- User-friendly web interface

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- PostgreSQL or SQLite

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/sohamgoswami07/Email-Storage.git
   cd email_storage_project
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   # on MAC use
   source venv/bin/activate
   # On Windows use
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up database migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (optional, for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open your browser and go to `http://127.0.0.1:8000/`

## Usage
1. Sign up or log in to your account.
2. Upload and store emails securely.
3. Retrieve and download emails when needed.
4. Manage stored emails through the dashboard.

## Configuration
- Environment variables can be set in a `.env` file (if using `django-environ`).
- Modify `settings.py` for database and other configurations.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
Created and developed by Soham Goswami.

## Contact
For issues or suggestions, open an issue on GitHub or put a mail on <a href="https://www.linkedin.com/in/soham-goswami-2a5b84143/">LinkedIn</a>.

