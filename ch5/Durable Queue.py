import rabbitpy

# Durable queue will be exist even if RabbitMQ restart
with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'durable-queue', durable=True)
        if queue.declare():
            print('Queue created')
