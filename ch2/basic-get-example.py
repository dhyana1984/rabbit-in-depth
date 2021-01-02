#!/usr/bin/env python

# Import the RabbitMQ Client Library
import rabbitpy

url = 'amqp://guest:guest@localhost:5672/%2F'

connection = rabbitpy.Connection(url)

channel = connection.channel()

queue = rabbitpy.Queue(channel, 'example')

# while there are messages in the queue, fetch them using Basic.Get
while len(queue) > 0:
    message = queue.get()
    print('Message:')
    print(' ID: %s' % message.properties['message_id'])
    print(' Time: %s' % message.properties['timestamp'].isoformat())
    print(' Body: %s' % message.body)
    message.ack()
