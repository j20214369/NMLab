import RPi.GPIO as GPIO
import time
from multiprocessing import Process, Manager

# input i = 1
# Pin Definitions
output_pin = 13  # BCM pin 18, BOARD pin 12
i = True


def choose_mode(i):
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    #GPIO.PWM(output_pin,50)
    print("Starting demo now! Press CTRL+C to exit")

    a = 1
    b = 1
    cycle = 0.02
    count = 0
    try:
        while True :
            #if(i.value == False):
                #time.sleep(0.01)
            #print("Running")
            time.sleep(0.015)#0.0176
            curr_value = GPIO.HIGH
            #print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, GPIO.HIGH)
            time.sleep(0.002)#0.0024
            curr_value = GPIO.LOW
            #print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, GPIO.LOW)
            count += 1

            if i.value == True:        
                x = 0.0055+0.003
                print("Unlock")
                while b<55:
                    if (b%2==0):
                        time.sleep(cycle - x+0.001)#0.009
                        curr_value = GPIO.HIGH
                        #print("Outputting {} to pin {}".format(curr_value, output_pin))
                        GPIO.output(output_pin, GPIO.HIGH)
                    else:
                        time.sleep(x-0.001)#0.007
                        curr_value = GPIO.LOW
                        #print("Outputting {} to pin {}".format(curr_value, output_pin))
                        GPIO.output(output_pin, GPIO.LOW)
                    b = b+1
                time.sleep(5)
                print("Finish sleep")
                b = 1
                x = 0.0055
                while b<55:
                    i.value = False
                    time.sleep(x +0.001)
                    curr_value = GPIO.HIGH
                    GPIO.output(output_pin, GPIO.HIGH)
                    time.sleep(cycle - x-0.001)
                    GPIO.output(output_pin, GPIO.LOW)
                    b += 1
                print("Finish reverse")
                b = 1
                count = 1

            if count % 165 == 0:
                #print('0')
                count = 0
                time.sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    manager = Manager()
    i = manager.Value('flag', True)

    choose_mode(i)

