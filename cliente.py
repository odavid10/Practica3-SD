import threading
import socket
import sys

def auth(miSocket, user):
    comando = "helloiam {}".format(user)
    
    miSocket.send(comando.encode())
    resp = miSocket.recv(1024)

    print(str(resp.decode()))
    
def comprobarLen():
    comando = "msglen"
    
    miSocket.send(comando.encode())
    resp = miSocket.recv(1024)

    print(str(resp.decode()))

    tmp = resp.decode().split()

    return int(tmp[1])

def getMensaje(tam):
    comando = 'givememsg 10000'

    miSocket.send(comando.encode())
    resp = miSocket.recv(tam)
    print(str(resp.decode()))

def chksum():
    comando = 'cheksum'

    miSocket.send(comando.encode())
    resp = miSocket.recv(tam)

    print(str(resp.decode()))
    
def bye():
    comando = 'bye'

    miSocket.send(comando.encode())
    resp = miSocket.recv(1024)

    print(str(resp.decode()))

def cliente():
    usuario = input("Indique el Usuario: ")
    auth(miSocket, usuario)
    tamMsg = int(comprobarLen())
    getMensaje(tamMsg)
    bye()

    miSocket.close()
    

miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
miSocket.connect((sys.argv[1], int(sys.argv[2])))

cliente()
