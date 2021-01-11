import datetime
import hashlib
import rabbitpy


with rabbitpy.Connection() as connection:
    with connection.channel() as channel:
        # Publish 100000 image as simulated
        for iteration in range(1000):
            timestamp = datetime.datetime.now().isoformat()
            # Use md5 as hash value
            hash_value = hashlib.md5()
            string = '%s: % s' % (timestamp, iteration)
            hash_value.update(string.encode('utf-8'))
            # if opinionated is ``True`` and the ``timestamp`` property is not specified when passing in ``properties``
            # the current Unix epoch value will be set in the message properties.
            msg = rabbitpy.Message(channel,
                                   'Image # %i' % iteration,
                                   {
                                       'headers':
                                       {
                                           'image-hash': str(hash_value.hexdigest())
                                       }
                                   },
                                   opinionated=True)
            msg.publish('image-storage')
