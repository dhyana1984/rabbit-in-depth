import rabbitpy
import time

'''
The condition for queue expiration
1. No cosumer connected. If there is any consomer connected, queue will be expired when get Basic.Cancel or disconnected
2. No Basic.Get request in TTL life cycle
3. x-expires value cannot be modified, if need to set to another value, just delete queue and create another with new x-expires
4. RabbitMQ cannot guarantee the timeliness for delete expired queue
'''
with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # arguments={'x-expires': 1000} define the queue expire time(TTL, Time To Live)
        queue = rabbitpy.Queue(channel, 'expiring-queue',
                               arguments={'x-expires': 1000})
        queue.declare()
        # passive=True is to retrieve message count and consumer count information
        messages, consumers = queue.declare(passive=True)
        time.sleep(2)
        try:
            messages, consumers = queue.declare(passive=True)
        except rabbitpy.exceptions.AMQPNotFound:
            print('The queue no longer exists')
