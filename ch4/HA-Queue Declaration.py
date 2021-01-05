import rabbitpy

# connect to RabbitMQ
connection = rabbitpy.Connection()
try:
    with connection.channel() as channel:
        # Create a new queue with HA policy
        # if publish message to HA queue, the message will be sent to all servers in cluster
        # if the message was consumed in any server, all message copy in other server will be deleted
        queue = rabbitpy.Queue(channel,
                               'my-ha-queue',
                               arguments={'x-ha-policy': 'all'})  # HA policy
        if queue.declare():
            print('Queue declared')
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print('Queue declare failed: %s' % error)
