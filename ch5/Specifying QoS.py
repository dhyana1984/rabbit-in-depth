import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # Prefetch count is QoS, before message was confirmed recieving, consumer can pre-recieve some messages(count)
        channel.prefetch_count(10)
        for message in rabbitpy.Queue(channel, 'test-message'):
            message.pprint()
            message.ack()
