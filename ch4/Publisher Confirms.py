#!/usr/bin/env python
import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        exchange = rabbitpy.Exchange(channel, 'chapter4-example')
        exchange.declare()
        # enable confirm
        channel.enable_publisher_confirms()
        message = rabbitpy.Message(channel,
                                   'There is an important message',
                                   {'content_type': 'text/plain',
                                    'message_type': 'very important'})
        # use confirm to verify if the message publish successfully
        if message.publish('chapter4-example', 'important.message'):
            print('The message was confirmed')
