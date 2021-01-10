import rabbitpy

'''
Topic exchange can route message by the route key rules
Using Topic exchange can silumate the direct exchange and fanout exchange
'''
with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        exchange = rabbitpy.Exchange(channel,
                                     'topic-rpc-requests',
                                     exchange_type='topic')
        exchange.declare()
