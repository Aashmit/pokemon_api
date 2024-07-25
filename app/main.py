# app/main.py
import asyncio
import httpx
from fastapi import FastAPI,Query,Depends
from app.database import init_db, engine, SessionLocal , get_session
from app.models import Pokemon
from app.crud import get_pokemons
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

app = FastAPI()

async def fetch_pokemon_details(url, client):
    for _ in range(3):  # Retry up to 3 times
        try:
            response = await client.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}. Retrying...")
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}. Retrying...")
        except httpx.TimeoutException as exc:
            print(f"Timeout while requesting {exc.request.url!r}. Retrying...")
    return None

async def fetch_and_store_pokemons():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://pokeapi.co/api/v2/pokemon?limit=100', timeout=10)
        pokemons = response.json()['results']

        async with AsyncSession(engine) as session:
            for pokemon in pokemons:
                details = await fetch_pokemon_details(pokemon['url'], client)
                if details:
                    new_pokemon = Pokemon(
                        name=details['name'],
                        image=details['sprites']['front_default'],
                        type=details['types'][0]['type']['name'] if details['types'] else 'unknown'
                    )
                    session.add(new_pokemon)
            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()
                print("Rolling back due to IntegrityError.")

@app.on_event("startup")
async def on_startup():
    await init_db()
    await fetch_and_store_pokemons()

@app.get("/api/v1/pokemons")
async def read_pokemons(
    name: str = Query(None, description="Filter by Pokémon name"),
    type: str = Query(None, description="Filter by Pokémon type"),
    session: AsyncSession = Depends(get_session)
):
    pokemons = await get_pokemons(session, name, type)
    return {
        "pokemons": [
            {
                "name": pokemon.name,
                "image": pokemon.image,
                "type": pokemon.type
            }
            for pokemon in pokemons
        ]
    }
