# Pokemon API with FastAPI and PostgreSQL

This project is a REST API for retrieving Pokémon data using the FastAPI framework and PostgreSQL as the database. It utilizes the PokeAPI to fetch Pokémon information and stores it in a PostgreSQL database. The API supports filtering Pokémon by name and type.

## Project Structure

- `app/`
  - `__init__.py` — Initializes the `app` module.
  - `config.py` — Contains configuration settings and environment variables.
  - `database.py` — Handles database connection and session management.
  - `models.py` — Defines the database models.
  - `crud.py` — Contains functions to interact with the database.
  - `main.py` — Main application file where the FastAPI app is defined and configured.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.9 or later
- PostgreSQL
- `pip` (Python package installer)

### Setting Up PostgreSQL

1. **Create a PostgreSQL Database

   ```sql
   CREATE DATABASE pokemon_db;
   ```
2. **Create a User**

   ```sql
   CREATE USER pokemon_user WITH PASSWORD 'password';
   ```
3. **Grant Privileges to User**

   ```sql
   GRANT ALL PRIVILEGES ON DATABASE pokemon_db TO pokemon_user;
   ```
4. **connect to the database**

   ```sql
   psql -U pokemon_user -d pokemon_db
   ```
5. **create the "pokemons table"**

   ```sql
   CREATE TABLE pokemons (
       id SERIAL PRIMARY KEY,
       name VARCHAR UNIQUE NOT NULL,
       image VARCHAR,
       type VARCHAR
   );
   ```
## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aashmit/pokemon_api.git
   cd pokemon_api
   ```
2. **Create and activate a virtual environment**
```python
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**:
pip install -r requirements.txt

4. **Update `app/config.py` with your database credenetials:**
```python
DATABASE_URL = "postgresql+asyncpg://pokemon_user:password@localhost/pokemon_db"
```
5. **Start your FASTAPI application which will automatically create the required tables:
```python
uvicorn app.main:app --reload
```
### Endpoints

-GET /api/v1/pokemons:
  -Retrieve a list of all Pokémon with their name, image, and type.
  -Include query parameters to filter by name and type:
    -name: Filter Pokémon by name.
    -type: Filter Pokémon by type.
