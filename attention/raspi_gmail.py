import RPi.GPIO as GPIO, feedparser
import time
USERNAME="notlarry.node@gmail.com"
PASSWORD="ppR14@33"
GPIO_PIN=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
if newmails > 0: 
	GPIO.output(GPIO_PIN, False)
        time.sleep (20)
else: 
	GPIO.output(GPIO_PIN, True)
        time.sleep (20)
