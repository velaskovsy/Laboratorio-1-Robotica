"""ControladorRobotLab1 controller."""
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Esto es para que el robot tenga velocidad infinita
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Main loop:
L = 0.052 # Distancia entre las ruedas
while robot.step(timestep) != -1:

    v = 4
    w = 30

    vl = v + (w * L) / 2 # velocidad en el motor izquierdo
    vr = v - (w * L) / 2 # velocidad en el motor derecho
    
    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)
    pass