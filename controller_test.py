import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print("Controller detected:", joystick.get_name())

while True:
    pygame.event.pump()

    x = joystick.get_axis(0)
    y = joystick.get_axis(1)

    print("X:", round(x,2), "Y:", round(y,2))
