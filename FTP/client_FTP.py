from socket import *
import sys
import time
import struct

# Realize various functional requests
class ftpClient(object):
    def __init__(self, sockfd):
        super().__init__()
        self.sockfd = sockfd
        self.opt = ''

    def panel(self):
        print('|', '-'*30, '-', sep='')
        print('|', 'display'.center(30), '|', sep='')
        print('|', 'download'.center(30), '|', sep='')
        print('|', 'upload'.center(30), '|', sep='')
        print('|', 'quit'.center(30), '|', sep='')
        print('|', '-'*30, '-', sep='')

    def display(self):
        self.sockfd.send(b'display')
        print(self.sockfd.recv(1024).decode())

    def download(self):
        'Client download request'
        filename = input('filename>> ')
        if not filename:
            return
        self.sockfd.send(b'display')
        files = self.sockfd.recv(1024).decode().split('\n')
        if not filename in files:
            print('Cannot locate', filename)
            return
       
        data = 'download ' + filename
        self.sockfd.send(data.encode())
        data = self.sockfd.recv(1024).decode()
        #  If the server cannot open the file
        if data == 'Failed to open file':
            print('Failed to open file')
       
        else:
   
            print(data)
            self.write(filename)
            print('received file!')

    def write(self, filename):
        'Download files from the server'
   
        fp = open(filename, 'wb')
        while True:
          
            res = self.sockfd.recv(4)
            length = struct.unpack('i', res)[0]
        
            if length == 0:
                break
    
            data = self.sockfd.recv(length)
            fp.write(data)
        fp.close()

    def upload(self):
        #  file path
        filepath = input('filepath>> ')
        try:
            fp = open(filepath, 'rb')
        except:
            print('Unable to open', filepath)
            return
        else:
    
            filename = input('filename>> ')
            if not filename:
                return
            self.sockfd.send(b'display')
            files = self.sockfd.recv(1024).decode().split('\n')
            if filename in files:
                print('File already exists!')
                return
            #  Can upload
            data = 'upload ' + filename
            self.sockfd.send(data.encode())
            data = self.sockfd.recv(1024).decode()
            if data == 'Unable to open file':
                print('Server opening file error')
                return 
            else:
                self.read(fp)

    def read(self, fp):
        'Read file upload server'
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

    def quit(self):
        self.sockfd.send(b'quit')
        self.sockfd.close()
        sys.exit('Client closed')

#  Create a socket, establish a connection
def main():
    argc = len(sys.argv)
    if argc != 3:
        sys.exit('Usage: python client.py host port')
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ADDR = HOST, PORT

        sockfd = socket()
        try:
            sockfd.connect(ADDR)
        except ConnectionRefusedError:
            sys.exit('Unable to connect to the server')

        ftp = ftpClient(sockfd)

        ftp.panel()
        while True:
            try:
                ftp.opt = input('>> ').lower()
            except KeyboardInterrupt:
                ftp.quit()
            if ftp.opt == 'display':
                ftp.display()
            elif ftp.opt == 'download':
                ftp.download()
            elif ftp.opt == 'upload':
                ftp.upload()
            elif ftp.opt == 'quit':
                ftp.quit()
            else:
                continue


if __name__ == '__main__':
    main()