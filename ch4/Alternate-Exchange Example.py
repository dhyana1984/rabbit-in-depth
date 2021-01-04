#!/usr/bin/env python
import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # Alternate exchange
        my_ae = rabbitpy.Exchange(channel, 'my-ae', exchange_type='fanout')
        my_ae.declare()
        # define the alternate exchange dict for graphite exchange
        args = {'alternate-exchange': my_ae.name}
        # create graphite exchange abd pass the args dict
        # If publish message to 'graphite' exchange and without valid route-key like message.publish('graphite','server-metrics'),
        # the message will publish to 'my-ae' exchange and 'unroutable-messages' queue
        exchange = rabbitpy.Exchange(channel,
                                     'graphite',
                                     exchange_type='topic',
                                     arguments=args)
        exchange.declare()

        # create a queue and bind to the alternate exchange
        queue = rabbitpy.Queue(channel, 'unroutable-messages')
        queue.declare()
        if queue.bind(my_ae, '#'):
            print('Queue bound to alternate-exchange')
