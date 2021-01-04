import datetime
import rabbitpy

# connect to RabbitMQ
with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        body = 'server.cpu.utilization 25.5 1350884514'
        message = rabbitpy.Message(channel,
                                   body,
                                   {'content_type': 'text/plain',
                                    'timestamp': datetime.datetime.now(),
                                    'message_type': 'graphite metric'})
        # Publish the message to the exchange with the routing key 'server-metrics'
        # mandatory=True will let RabbitMQ return a MessageReturnedException if publish failed
        message.publish('chapter2-example',
                        'server-metrics',
                        mandatory=True)
