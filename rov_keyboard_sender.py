import socket

UDP_IP = "192.168.1.20"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Keyboard Control")
print("w = UP")
print("s = DOWN")
print("f = FORWARD")
print("h = HOLD")
print("x = STOP")

while True:

    key = input("Enter key: ")
    key = key.lower()

    if key == "w":
        command = "UP"

    elif key == "s":
        command = "DOWN"

    elif key == "f":
        command = "FORWARD"

    elif key == "h":
        command = "HOLD"

    elif key == "x":
        command = "STOP"

    else:
        print("Invalid key")
        continue

    print("Sending:", command)

    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))
