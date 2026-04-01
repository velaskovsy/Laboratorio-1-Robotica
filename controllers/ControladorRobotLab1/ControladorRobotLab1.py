"""ControladorRobotLab1 controller."""
import random
from controller import Robot

robot = Robot()

timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# monitorear sensor encoder
left_sensor = robot.getDevice('left wheel sensor')
right_sensor = robot.getDevice('right wheel sensor')

# Esto es para que el robot tenga velocidad infinita
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_sensor.enable(timestep)
right_sensor.enable(timestep)

# Main loop:
L = 0.052 # Distancia entre las ruedas
while robot.step(timestep) != -1:

    v = 4
    w = 30

    vl = v + (w * L) / 2 # velocidad en el motor izquierdo
    vr = v - (w * L) / 2 # velocidad en el motor derecho
    
    perturbacion_l = random.uniform(-5, 5)
    perturbacion_r = random.uniform(-5, 5)
    
    left_motor.setVelocity(vl + perturbacion_l)
    right_motor.setVelocity(vr + perturbacion_r)
    
    pos_izq = left_sensor.getValue()
    pos_der = right_sensor.getValue()
    
    print(f"Encoder de la Izquierda: {pos_izq:.2f} - Encoder de la Derecha: {pos_der:.2f}")
    pass