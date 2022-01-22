import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 13  # BCM pin 18, BOARD pin 12

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")

    a = 1
    try:
        while a<70:
            if (a%2==0):
                time.sleep(0.009)
                curr_value = GPIO.HIGH
                print("Outputting {} to pin {}".format(curr_value, output_pin))
                GPIO.output(output_pin, GPIO.HIGH)
            else:
                time.sleep(0.007)
                curr_value = GPIO.LOW
                print("Outputting {} to pin {}".format(curr_value, output_pin))
                GPIO.output(output_pin, GPIO.LOW)
            a=a+1
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
