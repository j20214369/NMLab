import RPi.GPIO as GPIO
import time

# setup the GPIO pin for the servo
servo_pin = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin,GPIO.OUT,initial=GPIO.HIGH)



# setup PWM process
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

pwm.start(12) # start PWM by rotating to 90 degrees

for ii in range(0,3):
    print("ii")
    pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
    time.sleep(0.5)
    pwm.ChangeDutyCycle(12.0) # rotate to 180 degrees
    time.sleep(0.5)
    pwm.ChangeDutyCycle(7.0) # rotate to 90 degrees
    time.sleep(0.5)

pwm.ChangeDutyCycle(0) # this prevents jitter
pwm.stop() # stops the pwm on 13
GPIO.cleanup()
