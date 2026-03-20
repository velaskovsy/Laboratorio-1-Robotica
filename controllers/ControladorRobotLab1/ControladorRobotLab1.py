"""ControladorRobotLab1 controller."""
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

# Esto es para seguir la trayectoria del robot
pen = robot.getDevice('pen')
pen.write(1)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Esto es para que el robot tenga velocidad infinita
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Main loop:
while robot.step(timestep) != -1:

    vl = 3.0 # velocidad en el motor izquierdo
    vr = 3.0 # velocidad en el motor derecho
    
    left_motor.setVelocity(vl)
    right_motor.setVelocity(vr)
    pass