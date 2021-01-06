import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'test-message')
        queue.declare()
        # Get message by polling
        while True:
            message = queue.get()
            if message:
                message.pprint()
                message.ack()
                # Exit polling if the body is 'stop'
                if message.body.lower() == 'stop':
                    break
