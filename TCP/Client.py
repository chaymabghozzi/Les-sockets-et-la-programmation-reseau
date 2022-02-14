import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()

ip_address = socket.gethostbyname(local_hostname)

server_address = (ip_address, 9999)
print ('le démarrage sur %s le port %s' % server_address)
s.connect(server_address)

time.sleep(2)

s.sendall(str("host name= %s" % local_hostname).encode("utf-8"))

s.close ()