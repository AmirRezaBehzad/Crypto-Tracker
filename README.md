# Crypto Tracker
This is a small Django-based project built to help users track cryptocurrency deposits. It includes user registration/login and allows each user to view and add their own deposit records.
## Features
- Register and log in securely using Django's built-in authentication system
- Add and view personal cryptocurrency deposits (coin name, amount, date)
- Token-based authentication using `TokenAuthentication`
- Built with Django REST Framework (`APIView`)
- MySQL-compatible and `.env`-driven configuration
- Simple and clean codebase for learning or small-scale use
## Requirements
- Python 3.8+
- Django 4.x
- Django REST Framework
- `django-environ`
## Getting Started
### 1. Clone the repo
```bash
git clone https://github.com/AmirRezaBehzad/Crypto-Tracker.git
cd Crypto-Tracker
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Set up the .env file
Create a .env file in the root directory and fill it with your MySQL credentials:
```env
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306
```
### 5. Apply database migrations
```bash
python manage.py migrate
```
### 6. Run the server
```bash
python manage.py runserver
```
Visit http://127.0.0.1:8000/ to test the backend locally.

## API Endpoints

### Users

| Endpoint                | Method | Description             |
|-------------------------|--------|-------------------------|
| `/api/users/register/` | POST   | Register new users      |
| `/api/users/login/`    | POST   | Login and get token     |
| `/api/users/profile/`  | GET    | View logged-in user     |

### Deposits

| Endpoint          | Method | Description                  |
|-------------------|--------|------------------------------|
| `/api/deposits/`  | GET    | List user’s deposits         |
| `/api/deposits/`  | POST   | Add a new deposit record     |

> All deposit routes require `TokenAuthentication` via:
```http
Authorization: Token your_token_here
```

## Future Improvements

```markdown
Add Swagger or ReDoc API docs
Add support for more crypto fields (e.g., coin type, wallet address)
Add pagination and search filters
Add Docker and Docker Compose support
Create a simple React or HTML frontend
