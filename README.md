
This is underwater vehicle prototype for our mini project.

(We are now in the process of making  a version 2 of this vehicle for our final project with several advanced features.The goal is to make an autonomous underwater drone with mine seeking capabilites for the defense industry.)

# Tethered Underwater ROV (Mini Project)
## Overview

This project is a prototype of a **tethered underwater Remotely Operated Vehicle (ROV)** developed as part of our college mini project. The primary objective was to design and build a low-cost underwater drone capable of basic underwater maneuvering while being remotely controlled from a laptop through an Ethernet tether.

The project serves as a proof of concept for our final-year project, where additional features such as bidirectional thrusters, depth control, and autonomous navigation will be implemented.

---

## Features

- Tethered communication using Cat5 Ethernet cable
- Real-time control from a Windows laptop
- Raspberry Pi-based onboard controller
- Six BLDC thrusters controlled using ESCs
- Xbox controller and keyboard control support
- UDP-based communication between laptop and Raspberry Pi
- PWM motor control using the pigpio library

---

## Hardware Used

| Component | Quantity |
|----------|----------|
| Raspberry Pi 2 Model B | 1 |
| BLDC Motors | 6 |
| Unidirectional ESCs | 6 |
| Acrylic Pressure Tube | 1 |
| Cat5 Ethernet Cable | 1 |
| Xbox Controller | 1 |
| 3D Printed Frame | 1 |
| Propellers | 6 |

---

## Software Used

- Raspberry Pi OS
- Python 3
- Visual Studio Code
- pigpio
- socket (Python UDP communication)
- pygame-ce (Controller input)

---

## Project Architecture

```
Xbox Controller / Keyboard
            │
            ▼
      Windows Laptop
            │
     UDP Communication
            │
      Cat5 Ethernet Cable
            │
            ▼
      Raspberry Pi 2B
            │
        pigpio Library
            │
            ▼
      Electronic Speed Controllers
            │
            ▼
       BLDC Thrusters
```


---

## Motor Configuration

Our prototype uses:

- 4 Vertical Thrusters
  - Ascend
  - Descend
  - Maintain depth (constant thrust)

- 2 Horizontal Thrusters
  - Forward movement
  

Since only unidirectional ESCs were available for the mini project, reverse motion was not implemented. The ROV was designed with slight negative buoyancy so it naturally sinks slowly while the vertical thrusters provide lift for depth control.

---

Communication between the laptop and Raspberry Pi is achieved using UDP sockets over a direct Ethernet connection.

Example commands:

```

UP
DOWN
FORWARD
HOLD
STOP
```

The Raspberry Pi receives these commands and generates PWM signals to control the ESCs.

---

## Control Modes

### Keyboard


| Key | Action |
|------|--------|
| W | UP |
| S | DOWN |
| F | FORWARD |
| H | HOLD |
| X | STOP |

### Xbox Controller

Left joystick controls the movement of the ROV.

---

## Repository Structure


```
Laptop/
│
├── udp_sender.py
├── rov_keyboard_sender.py
├── rov_controller_sender.py

RaspberryPi/
│
├── rov_receiver.py
```

---
