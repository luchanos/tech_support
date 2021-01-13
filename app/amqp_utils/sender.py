import aio_pika


class AioPikaSender:
    """Simple sender for messages to RabbitMQ"""
    def __init__(self, host, user, password, routing_key):
        self.amqp_url = f"amqp://{user}:{password}@{host}"
        self.routing_key = routing_key
        self.connection = None

    async def setup(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)

    async def send(self, message):
        message = aio_pika.Message(body=message.encode())

        async with self.connection:
            channel = await self.connection.channel()

            await channel.default_exchange.publish(message=message,
                                                   routing_key=self.routing_key)
