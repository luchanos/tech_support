import pytest
import asyncpg


@pytest.fixture
async def db_pool():
    db_pool = await asyncpg.create_pool("0.0.0.0:8080/orders")
    yield db_pool
    await db_pool.close()
