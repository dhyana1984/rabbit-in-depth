import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        queue = rabbitpy.Queue(channel, 'expiring-msg-queue',
                               # Set dead_letter_exchange and x-message-ttl at the same time
                               # The expired message will transffer to DLX
                               dead_letter_exchange='rejected-messages',
                               arguments={'x-message-ttl': 1000})
        queue.declare()
