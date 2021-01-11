import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        for queue_num in range(4):
            queue = rabbitpy.Queue(channel, 'server%s' % queue_num)
            queue.declare()
            # Bind queue to the consistent hash exchange with weight 10
            queue.bind('image-storage', '10')
