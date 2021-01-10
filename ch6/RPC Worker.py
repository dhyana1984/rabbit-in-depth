from ch6 import utils
from ch6 import detect
import os
import rabbitpy
import time


connection = rabbitpy.Connection()
channel = connection.channel()
queue_name = 'rpc-worker-%s' % os.getpid()
# This worker queue should be close once consumer disconnect
# Only allow 1 consumer to connect this queue
# No persistent for this queue
queue = rabbitpy.Queue(channel, queue_name,
                       auto_delete=True,
                       durable=False,
                       exclusive=True)
if queue.declare():
    print('Worker queue declared')
# Bind to direct exchange with route key
# if queue.bind('direct-rpc-requests', 'detect-faces'):
#     print('Worker queue bound')

# Bind to fanout exchange without any route key
if queue.bind('fanout-rpc-requests'):
    print('Worker queue bound')

# Bind to Topic Exchange with specific route key rule
# if queue.bind('topic-rpc-requests', 'image.new.*'):

for message in queue.consume_messages():
    # Print the time cost for getting the message
    duration = (
        time.time() - int(message.properties['timestamp'].strftime('%s')))
    print('Received RPC request published %.2f seconds ago' % duration)

    # Write the message body to a temp file
    temp_file = utils.write_temp_file(
        message.body, message.properties['content_type'])

    # Detect faces. detect.faces() will return the new files which was detected
    result_fille = detect.faces(temp_file)

    # Build the properties for response message
    properties = {
        'app_id': 'CH6 Listing 2 Consumer',
        'content_type': message.properties['content_type'],
        'correlation_id': message.properties['correlation_id'],
        'headers': {
            'first_publish': message.properties['timestamp']
        }
    }

    # Build the body for response message
    body = utils.read_image(result_fille)
    # Delete the temp file and result file
    os.unlink(temp_file)
    os.unlink(result_fille)

    # Create the response message and publish response message
    response = rabbitpy.Message(channel, body, properties)
    # message.properties['reply_to'] is the response queue's route key
    response.publish('rpc-replies', message.properties['reply_to'])
