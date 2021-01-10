import os
import hashlib
import rabbitpy

connection = rabbitpy.Connection()
channel = connection.channel()
queue_name = 'hashing-worker-%s' % os.getpid()
# This worker queue should be close once consumer disconnect
# Only allow 1 consumer to connect this queue
# No persistent for this queue
queue = rabbitpy.Queue(channel, queue_name,
                       auto_delete=True,
                       durable=False,
                       exclusive=True)
if queue.declare():
    print('Worker queue declared')

if queue.bind('fanout-rpc-requests'):
    print('Worker queue bound')

for message in queue.consume_messages():
    hash_obj = hashlib.md5(message.body)
    # Print out the info, this might go into a database or log file
    # When client publish a message to fanout-rpc-requests exchange,
    # the fanout exchage will deliver message to all the queues bind to fanout exchange
    # The Worker Consumer will handle image identity, and this Hash Consumer will handle image Hash
    print('Image with correlation-id of %s has a hash of %s' %
          (message.properties['correlation_id'],
           hash_obj.hexdigest()))
    message.ack()
