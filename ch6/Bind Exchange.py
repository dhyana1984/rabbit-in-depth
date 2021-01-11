import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        tpc = rabbitpy.Exchange(channel, 'events', exchange_type='topic')
        tpc.declare()
        xch = rabbitpy.Exchange(
            channel, 'distributed-events', exchange_type='x-consistent-hash')
        xch.declare()
        # Bind xch exchange to the topic exchange
        xch.bind(tpc, '#')
