import rabbitpy

with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # define transaction
        tx = rabbitpy.Tx(channel)
        # start transaction
        tx.select()
        message = rabbitpy.Message(channel,
                                   'There is an important message',
                                   {'content_type': 'text/plain',
                                    'delivery_mode': 2,
                                    'message_type': 'very important'})
        message.publish('chapter4-example', 'important.message')
        try:
            if tx.commit():
                print('Transaction comitted')
        except rabbitpy.exceptions.NoActiveTransactionError:
            print('Tried to commit without active transaction')
