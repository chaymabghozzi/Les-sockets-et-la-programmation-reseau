import socket
import getopt
import sys


login = ''
host = ''

argv = sys.argv[1:]

print('ARGV  :',argv[1:])

try:
   opts, args = getopt.gnu_getopt(sys.argv[1:], 'l:h', ['login=', 'host='])
except getopt.GetoptError:
   print('erreur')
   sys.exit(2)


print(opts)
    
for opt, arg in opts:
   if opt in['-h', '--host']: 
      HOST = arg  # The server's hostname or IP address

PORT = 7979 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    for opt, arg in opts:
        if opt in['-l', '--login']:
            s.sendall(str("%s" % arg).encode("utf-8"))
            data = s.recv(1024)
            print(data.decode())
    print( login +" "+host)