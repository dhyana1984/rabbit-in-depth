#!/usr/bin/env python

# Import the RabbitMQ Client Library
import rabbitpy

# Specify the URL to connect to
url = 'amqp://guest:guest@localhost:5672/%2F'

# Connect to RabbitMQ using the URL above
connection = rabbitpy.Connection(url)

