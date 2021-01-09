import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # auto_delete = True, this queue will delete itself when consumer disconnect
        queue = rabbitpy.Queue(channel, 'ad-example', auto_delete=True)
        queue.declare()
