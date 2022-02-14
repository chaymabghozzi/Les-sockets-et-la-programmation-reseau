import struct
from socket import *
import os
import signal
import sys
import time


FILE_PATH =  '/home/chayma/Bureau/chayma/'

class ftpServer(object):
    def __init__(self, sockfd, addr):
        super().__init__()
        self.sockfd = sockfd
        self.addr = addr
        self.opt = ''

    def display(self):
        re = ''
        for i in os.listdir(FILE_PATH):
            re += i + '\n'
        self.sockfd.send(re.encode())

    def download(self):
        'Download module function realization'
        #  open the file
        filename = FILE_PATH + self.opt.split(' ')[1]
        print(filename)
        try:
            fp = open(filename, 'rb')
        except:
            self.sockfd.send(b'Failed to open file')
        else:
            self.sockfd.send(b'Ready to transfer')
            #  Send data 
            while True:        
                data = fp.read(1024)        
                if not data:
                  
                    res = struct.pack('i', 0)
                    self.sockfd.send(res)
                    break
                res = struct.pack('i', len(data))
                self.sockfd.send(res)
                self.sockfd.send(data)
            print('Done!')

    def upload(self):
        filename = FILE_PATH + self.opt.split(' ')[1]
        try:
            fp = open(filename, 'wb')
        except:
            self.sockfd.send('Unable to open file'.encode())
        else:
            self.sockfd.send(b'Ready to upload')
            while True:
                res = self.sockfd.recv(4)
                length = struct.unpack('i', res)[0]
                if length == 0:
                    break
                data = self.sockfd.recv(length)
                fp.write(data)
            fp.close()
            print('Done!')


    def quit(self):
        print(self.addr, 'Disconnect')
        self.sockfd.close()
        sys.exit()

#  Main process
def main():
    HOST = '127.0.0.1'
    PORT = 2525
    ADDR = (HOST, PORT)

    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(5)

   
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit('Server exit')
        except Exception as e:
            print(e)
            continue

        print('connection succeeded:', addr)

        #  Create child process
        pid = os.fork()

        if pid == 0:
            sockfd.close()
            ftp = ftpServer(connfd, addr)
            while True:
                ftp.opt = connfd.recv(1024).decode()
                if ftp.opt == 'display':
                    ftp.display()
                elif ftp.opt.startswith('download'):
                    ftp.download()
                elif ftp.opt.startswith('upload'):
                    ftp.upload()
                elif ftp.opt == 'quit':
                    ftp.quit()
        else:
            connfd.close()
            continue


if __name__ == '__main__':
    main()