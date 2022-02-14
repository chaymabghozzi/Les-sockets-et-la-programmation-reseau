import socket
 
msgFromClient       = "Bonjour Serveur UDP"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 9875)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message du serveur {}".format(msgFromServer[0])
print(msg)
UDPClientSocket.close()
print ("fin du client UDP")