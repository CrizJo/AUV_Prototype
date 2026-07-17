import socket
import time

# Raspberry Pi IP address
UDP_IP = "192.168.1.20"
UDP_PORT = 5005

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = "Hello from laptop"

    # Send message to Raspberry Pi
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))

    print("Sent:", message)

    time.sleep(1)
