import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        for message in rabbitpy.Queue(channel, 'test-message'):
            message.pprint()
            message.ack()
            # Should use message.body.decode() to convert bytearray body to string
            if message.body.decode() == 'stop':
                print('stopped')
                # When break and exit
                # 1.Client send Basic.Cancel to RabbitMQ
                # 2.RabbitMQ return Basic.ConcelOk to client
                # 3.If there is any message sent by client without response, client will send a Basic.Nack to RabbitMQ
                # 4.RabbitMQ resend the response.
                break
