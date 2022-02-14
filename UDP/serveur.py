import socket

 
localIP= "127.0.0.1"
localPort= 9875
bufferSize= 1024

msgFromServer= "Bonjour Client UDP"

bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, 9875))
print("Serveur UDP en place et en écoute")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message du client :{}".format(message)
    clientIP  = "Adresse IP du client :{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
    