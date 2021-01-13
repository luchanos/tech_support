import aio_pika


class AioPikaSender:
    """Simple sender for messages to RabbitMQ"""
    def __init__(self, host, user, password):
        self.amqp_url = f"amqp://{user}:{password}@{host}"
        self.connection = None
        self.channel = None

    async def setup(self):
        await self._connect()

    async def _connect(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()

    async def send(self, message, routing_key, exchange=''):
        message = aio_pika.Message(body=str(message).encode())
        exchange = await self.channel.get_exchange(name=exchange)
        await exchange.publish(message, routing_key=routing_key)

    async def send(self, message):
        message = aio_pika.Message(body=message.encode())

        async with self.connection:
            channel = await self.connection.channel()

            await channel.default_exchange.publish(message=message,
                                                   routing_key=self.routing_key)
