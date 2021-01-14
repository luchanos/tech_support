CREATE_ORDER_QUERY = """INSERT INTO orders (agent_id, message, serial_no, status) 
VALUES ($1, $2, $3, $4) RETURNING order_id"""

DELETE_ORDER_QUERY = """DELETE FROM orders WHERE order_id = $1"""


class OrdersManager:
    """
    Class for managing orders way
    """
    def __init__(self, db_orders_pool):
        self.db_orders_pool = db_orders_pool

    async def create_order(self, agent_id: int, message: str, serial_no: str, status: int):
        return await self.db_orders_pool.fetchval(CREATE_ORDER_QUERY, agent_id, message, serial_no, status)

    async def delete_order(self, order_id):
        await self.db_orders_pool.fetch(DELETE_ORDER_QUERY, order_id)
