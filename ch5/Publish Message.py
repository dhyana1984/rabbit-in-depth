import rabbitpy

for iteration in range(15):
    rabbitpy.publish('amqp://guest:guest@localhost:5672/%2f',
                     '', 'ad-example', 'go')
rabbitpy.publish('amqp://guest:guest@localhost:5672/%2f',
                 '', 'ad-example', 'stop')
