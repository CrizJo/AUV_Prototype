import socket

UDP_IP = "192.168.1.20"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    command = input("Enter command: ")

    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
