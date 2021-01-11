import pytest
import asyncpg


@pytest.fixture
async def db_pool():
    db_pool = await asyncpg.create_pool("postgres://postgres:dbpass@0.0.0.0:5432/db")
    yield db_pool
    await db_pool.close()
