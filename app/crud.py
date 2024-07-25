from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Pokemon

async def get_pokemons(session: AsyncSession, name: str = None, type: str = None):
    query = select(Pokemon)
    
    # Add filters based on provided parameters
    if name:
        query = query.filter(Pokemon.name.ilike(f'%{name}%'))
    if type:
        query = query.filter(Pokemon.type.ilike(f'%{type}%'))

    result = await session.execute(query)
    return result.scalars().all()
