# Blog API

REST API for a blog built with FastAPI: user signup/login with JWT, full CRUD for posts, SQLAlchemy, PostgreSQL and Alembic.

## Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – Database
- **Alembic** – Migrations
- **PyJWT** – JWT auth
- **bcrypt** – Password hashing
- **Pydantic** – Validation & settings

## Requirements

- Python 3.12+
- PostgreSQL

## Setup

1. **Clone and enter the project**

   ```bash
   cd blogAPI
   ```

2. **Create a virtual environment and install dependencies**

   ```bash
   python -m venv env
   source env/bin/activate   # Linux/macOS
   # env\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```

3. **Environment variables**

   Create a `.env` file in the project root (see `.env.example` if available, or use):

   ```env
   DB_NAME=your_db_name
   DB_USERNAME=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   SECRET_KEY=your_secret_key
   ```

   For production, set `APP_ENV=prod` so the app loads `.env.prod` instead.

4. **Database**

   Create the PostgreSQL database, then run migrations:

   ```bash
   alembic upgrade head
   ```

5. **Run the API**

   ```bash
   python app.py
   ```

   Or with uvicorn:

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8080 --reload
   ```

   API: **http://localhost:8080**  
   Interactive docs: **http://localhost:8080/docs**

## API Overview

### Auth (no token)

| Method | Endpoint        | Description   |
|--------|-----------------|---------------|
| POST   | `/user/signup`  | Register user |
| POST   | `/user/login`   | Login, returns JWT |

### Posts (Bearer token required)

| Method | Endpoint             | Description        |
|--------|----------------------|--------------------|
| POST   | `/post/post`         | Create post        |
| GET    | `/post/posts`        | List all posts     |
| GET    | `/post/post/{id}`    | Get one post       |
| PUT    | `/post/post/{id}`    | Update post (owner) |
| DELETE | `/post/post/{id}`    | Delete post (owner) |

### Auth header

After login, send the token in the header:

```
Authorization: Bearer <access_token>
```

## Project structure

```
blogAPI/
├── app.py              # FastAPI app entry
├── config.py           # Settings (env)
├── database.py         # SQLAlchemy engine & session
├── dependencies.py     # FastAPI dependencies (DB, current user)
├── alembic/            # Migrations
├── core/
│   ├── user/           # User model, routes, schema, JWT
│   └── post/           # Post model, routes, schema
└── tests/              # Pytest tests
```

## Tests

```bash
pytest
```

## License

MIT
