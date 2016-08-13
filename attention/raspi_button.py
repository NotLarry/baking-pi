import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_PIN=17
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, True)
while True:
    input_state = GPIO.input(23)
    if input_state == False:
	GPIO.output(GPIO_PIN, False)

