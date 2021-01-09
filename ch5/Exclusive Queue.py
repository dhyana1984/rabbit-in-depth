import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # exclusive=True will auto delete queue when consumer disconnect, but only allow 1 channel
        # Only the first time connected consomer can connect to this queue
        queue = rabbitpy.Queue(channel, 'exclusive-example', exclusive=True)
        queue.declare()
