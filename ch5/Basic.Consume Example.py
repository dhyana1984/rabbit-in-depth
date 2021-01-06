import rabbitpy

# Consume mode to read the messages in queue
for message in rabbitpy.consume('amqp://guest:guest@localhost:5672/%2f', 'test-message'):
    message.pprint()
    message.ack()
