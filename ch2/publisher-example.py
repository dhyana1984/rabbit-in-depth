#!/usr/bin/env python

# Import the RabbitMQ Client Library
import rabbitpy

# specify the url to connect to RabbitMQ service
url = 'amqp://guest:guest@localhost:5672/%2F'

# connect to RabbitMQ
connection = rabbitpy.Connection(url)

# Open a new channel on the connection
channel = connection.channel()

# Crete a new exchange object, passing in the channel to use
exchange = rabbitpy.Exchange(channel, 'chapter2-example')

# Declare the exchange on the RabbitMQ server
exchange.declare()

# create a new queue object, passing in the channel to use
queue = rabbitpy.Queue(channel, 'example')

# declare the queue on the RabbitMQ server
queue.declare()

# Bind the queue to the exchange on the RabbitMQ server
queue.bind(exchange, 'example-routing-key')

for message_number in range(0, 10):
    message = rabbitpy.Message(channel,
                               'Test message #%i' % message_number,
                               {'content_type': 'text/plain'},
                               opinionated=True)
    message.publish(exchange, 'example-routing-key')

input('wait')
