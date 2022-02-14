import socket

# creation d'une socket TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# récupérer le nom d'hôte local
local_hostname = socket.gethostname()

# obtenir l'adresse IP correspondante
ip_address = socket.gethostbyname(local_hostname)

print ("travailler sur %s avec %s" % (local_hostname, ip_address))

# bind la socket au port 9999
server_address = (ip_address, 9999)
print ("démarrage sur l'adresse %s et le port %s" % server_address)
serversocket.bind(server_address)

# écouter les connexions entrantes (mode serveur) avec une seule connexion à la fois
serversocket.listen(1)

while True:
    # attendre une connexion
    print ('attente d une connexion')
    connection, client_address = serversocket.accept()

    try:
        print ('connection from', client_address)

        while True:
            data = connection.recv(1024)
            if data:
                print ("les données: %s" % data)
            else:
                print ("pas de données")
                break
    finally:
        connection.close()