import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        channel.prefetch_count(10)
        # define a unack counter
        unacknoledged = 0
        for message in rabbitpy.Queue(channel, 'test-message'):
            message.pprint()
            unacknoledged += 1
            if unacknoledged == 10:
                # if unack counter is 10, confirm all the message before
                # confirm multiple messages that pre-fetched
                message.ack(all_previous=True)
                unacknoledged = 0
