# Task Manager REST API with Authentication

## Project Description
This project is a RESTful API for managing tasks using Python Flask. It provides user registration, login, and secure task management using JWT authentication.

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Bcrypt
- SQLite
- Thunder Client

## Features
- User registration
- User login
- Password hashing
- JWT-based authentication
- Create tasks
- View all tasks
- Update tasks
- Delete tasks
- User-specific task management
- Protected API endpoints

## Project Structure
```text
TaskManagerAPI/
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── extensions.py
│   ├── models.py
│   └── tasks.py
├── config.py
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start the Flask application:

```bash
python run.py
```

The server runs at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/auth/register | Register a user |
| POST | /api/auth/login | Login and receive JWT |
| POST | /api/tasks/ | Create a task |
| GET | /api/tasks/ | View all tasks |
| PUT | /api/tasks/1 | Update a task |
| DELETE | /api/tasks/1 | Delete a task |

## Authentication

Task management endpoints require a valid JWT access token.

Add this header to protected requests:

`Authorization: Bearer YOUR_ACCESS_TOKEN`

## Testing
The APIs were tested using Thunder Client in Visual Studio Code.

## Database
SQLite is used to store user and task information. Passwords are stored as hashed values.

## Conclusion
This project demonstrates REST API development, CRUD operations, database integration, user authentication, and secure access control using Flask.