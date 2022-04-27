import socket
import sys

msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

addr = ('localhost', int(sys.argv[1]))

UDP_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDP_socket.sendto(bytesToSend, addr)

