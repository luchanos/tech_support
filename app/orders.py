CREATE_ORDER_QUERY = """INSERT INTO orders (agent_id, message, serial_no, status) 
VALUES ($1, $2, $3, $4) RETURNING order_id"""


class OrdersManager:
    """
    Class for managing orders way
    """

    async def create_order(self, db_orders_pool, agent_id: int, message: str, serial_no: str, status: int):
        return await db_orders_pool.fetchval(CREATE_ORDER_QUERY, agent_id, message, serial_no, status)
