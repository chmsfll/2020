from spike import MotorPair
motors = MotorPair ('A', 'E')
#To write a moving line, you do: motors.move(How many cenitmeters, 'cm', the angle, and then the power)
motors.move(42, 'cm', 0, 50)
motors.move(25, 'cm', -45, 50)
motors.move(10, 'cm', 0, 50)
motors.move(15, 'cm', -45, 50)
motors.move(14, 'cm', 0, 50)
motors.move(2, 'cm', 0, 50)
motors.move(2, 'cm', 0, -50)
motors.move(2, 'cm', 0, 50)
motors.move(2, 'cm', 0, -50)
motors.move(2, 'cm', 0, 50)
motors.move(2, 'cm', 0, -50)
