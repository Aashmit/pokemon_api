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
