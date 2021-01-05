import rabbitpy

# connect to RabbitMQ
connection = rabbitpy.Connection()
try:
    with connection.channel() as channel:
        # HA set not to accross all the servers in cluster but set some node
        arguments = {
            'x-ha-policy': 'nodes',
            'x-ha-nodes': ['rabbit@node1', 'rabbit@node2', 'rabbit@node3']
        }
        queue = rabbitpy.Queue(channel, arguments=arguments)
        if queue.declare():
            print('Queue declared')
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print('Queue declare failed: %s' % error)
