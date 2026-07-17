import socket
import pygame
import time

UDP_IP = "192.168.1.20"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Controller connected:", joystick.get_name())

deadzone = 0.25
last_command = None

while True:

    pygame.event.pump()

    x = joystick.get_axis(0)
    y = joystick.get_axis(1)

    command = None

    # LEFT = stop everything
    if x < -0.6:
        command = "STOP"

    # RIGHT = forward
    elif x > 0.6:
        command = "FORWARD"

    # UP = ascend
    elif y < -0.6:
        command = "UP"

    # DOWN = descend
    elif y > 0.6:
        command = "DOWN"

    # CENTER = hold altitude
    elif abs(x) < deadzone and abs(y) < deadzone:
        command = "HOLD"

    # send command only if it changed
    if command != last_command and command is not None:

        print("Sending:", command)
        sock.sendto(command.encode(), (UDP_IP, UDP_PORT))

        last_command = command

    time.sleep(0.1)
