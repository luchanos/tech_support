import aio_pika


class AioPikaConsumer:
    def __init__(self, host, user, password, routing_key):
        self.amqp_url = f"amqp://{user}:{password}@{host}"
        self.routing_key = routing_key
        self.connection = None

    async def setup(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)

    async def get_message(self, queue_name):
        channel = await self.connection.channel()
        queue = await channel.declare_queue(queue_name, auto_delete=False, durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)
