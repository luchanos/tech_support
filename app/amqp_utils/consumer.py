import aio_pika


class AioPikaConsumer:
    def __init__(self, host, user, password, routing_key):
        self.amqp_url = f"amqp://{user}:{password}@{host}"
        self.routing_key = routing_key
        self.connection = None

    async def _connect(self):
        self.connection = await aio_pika.connect_robust(self.amqp_url)
        self.channel = await self.connection.channel()

    async def setup(self):
        await self._connect()

    async def get_message(self, queue_name):
        queue = await self.channel.declare_queue(queue_name, auto_delete=False, durable=True)

        # todo luchanos - here is auto ack! Needs to be done with manual ack.
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)
