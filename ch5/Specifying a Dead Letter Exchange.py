import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # Declare the DLX
        dlx = rabbitpy.Exchange(channel, 'rejected-messages')
        dlx.declare()

        queue = rabbitpy.Queue(channel, 'dlx-example',
                               # dead_letter_exchange='rejected-messages' will add a x-dead-letter-exchange:rejected-messages feature in queue
                               dead_letter_exchange='rejected-messages',
                               # define the dead_letter_routing_key is very important
                               dead_letter_routing_key='dlx')
        queue.declare()
        # bind this queue to dead_letter_routing_key, then the rejected message will send to this queue
        queue.bind(dlx, 'dlx')

        # This is a common queue
        # Must set dead_letter_exchange and dead_letter_routing_key, then DLX will work
        queue2 = rabbitpy.Queue(channel, 'reject-example',
                                # Set the DLX as 'rejected-messages'
                                dead_letter_exchange='rejected-messages',
                                # Set the dead_letter_routing_key as the same as 'dlx-example' queue
                                dead_letter_routing_key='dlx')
        queue2.declare()
