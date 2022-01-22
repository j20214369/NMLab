import RPi.GPIO as GPIO
import time
# input i = 1
# Pin Definitions
output_pin = 13  # BCM pin 18, BOARD pin 12
i = True

def choose_mode(i):
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")

    a = 1
    b = 1
    try:
        while True :
            if (a%2==0):
                time.sleep(0.0176)
                curr_value = GPIO.HIGH
                print("Outputting {} to pin {}".format(curr_value, output_pin))
                GPIO.output(output_pin, GPIO.HIGH)
            else:
                time.sleep(0.0024)
                curr_value = GPIO.LOW
                print("Outputting {} to pin {}".format(curr_value, output_pin))
                GPIO.output(output_pin, GPIO.LOW)
            a = a+1
            if (i == True):        
                while b<70:
                    if (b%2==0):
                        time.sleep(0.009)
                        curr_value = GPIO.HIGH
                        print("Outputting {} to pin {}".format(curr_value, output_pin))
                        GPIO.output(output_pin, GPIO.HIGH)
                    else:
                        time.sleep(0.007)
                        curr_value = GPIO.LOW
                        print("Outputting {} to pin {}".format(curr_value, output_pin))
                        GPIO.output(output_pin, GPIO.LOW)
                    b = b+1
                time.sleep(10)
                b = 1
                i = False
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    choose_mode(i)

