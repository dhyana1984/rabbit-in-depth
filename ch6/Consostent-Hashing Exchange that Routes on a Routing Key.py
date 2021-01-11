import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # Create consistent hash exchange
        exchange = rabbitpy.Exchange(channel, 'image-storage',
                                     exchange_type='x-consistent-hash')
        exchange.declare()
