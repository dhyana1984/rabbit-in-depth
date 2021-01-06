import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'test-message')
        for message in queue.consume_messages(no_ack=True):
            message.pprint()
