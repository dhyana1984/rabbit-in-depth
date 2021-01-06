import rabbitpy

for iteration in range(15):
    rabbitpy.publish('amqp://guest:guest@localhost:5672/%2f',
                     '', 'test-message', 'go')
rabbitpy.publish('amqp://guest:guest@localhost:5672/%2f',
                 '', 'test-message', 'stop')
