import datetime
import rabbitpy

# connect to RabbitMQ
connection = rabbitpy.Connection()
try:
    with connection.channel() as channel:
        properties = {'content_type': 'text/plain',
                      'timestamp': datetime.datetime.now(),
                      'message_type': 'graphite metric'}
        body = 'server.cpu.utilization 25.5 1350884514'
        message = rabbitpy.Message(channel, body, properties)

        message.publish('chapter2-example',
                        'server-metrics',
                        mandatory=True)
except rabbitpy.exceptions.MessageReturnedException as error:
    print('publish failure: %s' % error)
