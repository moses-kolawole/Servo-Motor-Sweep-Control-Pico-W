import machine
from time import sleep as s
servopin = 15
servo = machine.PWM(machine.Pin(servopin))
servo.freq(50)
counter = 0

while True:
    counter = counter + 255
    servo.duty_u16(counter)
    if (counter > 8191):
        counter = 0
    s(0.1)

        