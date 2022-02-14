
import socket
import subprocess
import os
import sys
import getopt, sys

HOST = '127.0.0.1'  
PORT = 7979

def get_pid ():
    with open('/tmp/finger.pid', 'w') as f:
        pid=os.getpid()
        print('pid:', pid, file=f)
        f.close
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    get_pid()
    s.bind((HOST, PORT))
    s.listen(1)
    #print ('attente d une connexion:')
    conn, addr = s.accept()
    with conn:
        
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)            
            if not data:
                break
            data = data.decode('utf-8')
            commande = "finger " + data
            res = subprocess.getoutput(commande)
            conn.sendall(res.encode())

            with open('/tmp/finger.log','w') as f:
                 print('Login', data, file=f)
                 print('adresse client', addr, file=f)
                 f.close
   
            msg=subprocess.getoutput(data)
            conn.send(msg.encode())
            data = conn.recv(1024)
            if len(data)==0:
               print('message reçu')
