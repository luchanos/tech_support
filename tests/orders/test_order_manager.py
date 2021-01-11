import asyncpg
import pytest


@pytest.mark.asyncio
async def test_create_order(db_pool):
    GET_ORDER_FROM_DATABASE = """SELECT * FROM orders WHERE order_id = $1"""

    order_manager = OrderManager()
    order_id = await order_manager.create_order(agent_id=1, message="some malfunction message", serial_no=123)
    order_from_db = await db_pool.fetch(GET_ORDER_FROM_DATABASE, order_id)
    assert len(order_from_db) == 1
    assert order_id == order_from_db[0]["order_id"]
