import rabbitpy

connection = rabbitpy.Connection()
# Check if client was blocked
print('Connection is Blocked? %s' % connection.blocked)
