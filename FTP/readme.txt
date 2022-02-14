Client FTP:
./client_FTP.py 127.0.0.1 2525  

serveur de fichiers ftp

 Fonction de projet :
    *   Le client dispose d'une simple invite de commande de page
     * Les   fonctionnalités incluent :
         1. Afficher la liste des fichiers dans la bibliothèque de fichiers du serveur (fichiers communs) -> os.listdir
         2 , Vous pouvez télécharger l'un des fichiers sur le local
         3 , Vous pouvez télécharger les fichiers client dans la bibliothèque de fichiers du serveur
     *   Exigences du serveur :
         1 , Permettre à plusieurs clients de fonctionner en même temps
         2 , Chaque client peut envoyer des commandes en continu

 analyse technique: 
    1 , les sockets TCP sont plus adaptées au transfert de fichiers
     2. Schéma de concurrence -> Concurrence   multi-processus Fork
     3 , Opérations de lecture et d'écriture sur les fichiers
     4. Obtenir la liste des fichiers ->   os.listdir() ou arbre
     5 , Le traitement des sacs collants

 Conception globale de la structure :
    1 , La fonction serveur est encapsulée dans la classe (upload, download, view list)
     2 , Créer une socket, la fonction process appelle main()
     3 , Le client est responsable de l'initiation des requêtes, de la réception des réponses et de l'affichage
     4 , Le serveur est responsable de l'acceptation des demandes et du traitement logique

 Réalisation de la programmation :
    1 , Construire la structure globale, créer des connexions réseau
     2 , Créer une structure multi-processus et de classe
     3 , La réalisation de chaque module fonctionnel

 Méthode du module :
    os.listdir(chemin)
    os.path.isfile()
    os.path.isdir()