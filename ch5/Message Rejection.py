import rabbitpy

for message in rabbitpy.consume('amqp://localhost:5672/#/queues/%2F/ad-example', 'ad-example'):
    message.pprint()
    # If reject message, message.redelivered will be True
    print('Redelevered: %s' % message.redelivered)
    # message.reject(True) means requeue the message, the message could be consume again.
    message.reject()
    # If message.reject(True) to set as redeliver the message, the message will not transffer to DLX
    # message.reject(True)
