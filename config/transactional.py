from functools import wraps
from sqlalchemy.ext.asyncio import AsyncSession


def transactional(func):
    @wraps(func)
    async def wrapper(*args, db: AsyncSession, **kwargs):
        async with db.begin():
            result = await func(*args, db=db, **kwargs)
        return result
    return wrapper
