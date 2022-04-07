# TCP - Transport Control Protocol
# Sockets - bidirectional flow of data (data phone call)
# TCP port numbers- like a area code

import socket
# phone number
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone call
mysock.connect(('data.pr4e.org', 80))
mysock.close()
