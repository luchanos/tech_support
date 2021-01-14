import pytest
from app.orders import OrdersManager

GET_ORDER_FROM_DATABASE = """SELECT * FROM orders WHERE order_id = $1"""
CREATE_ORDER_QUERY = """INSERT INTO orders (agent_id, message, serial_no, status) 
VALUES ($1, $2, $3, $4) RETURNING order_id"""


async def create_order_in_database(db_pool, agent_id, message, serial_no, status):
    res = await db_pool.fetch(CREATE_ORDER_QUERY, agent_id, message, serial_no, status)
    return res[0]['order_id']


@pytest.mark.asyncio
async def test_create_order(db_pool):
    order_manager = OrdersManager(db_pool)
    order_id = await order_manager.create_order(
                                                agent_id=1,
                                                message="some malfunction message",
                                                serial_no="A123",
                                                status=1)
    order_from_db = await db_pool.fetch(GET_ORDER_FROM_DATABASE, order_id)
    assert len(order_from_db) == 1
    assert order_id == order_from_db[0]["order_id"]


@pytest.mark.asyncio
async def test_delete_order(db_pool):
    order_id = await create_order_in_database(db_pool=db_pool,
                                              agent_id=1,
                                              message="some malfunction message",
                                              serial_no="A123",
                                              status=1)
    order_manager = OrdersManager(db_pool)
    await order_manager.delete_order(order_id)
    orders = await db_pool.fetch(GET_ORDER_FROM_DATABASE, order_id)
    assert len(orders) == 0
