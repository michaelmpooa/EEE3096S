import time
import RPi.GPIO as GPIO

begin = time.time()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

count = 0b000
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ledbulb_plus(channel):
	global count
	count = count +1
        GPIO.output(11,(count & (1 << 0) == 1))
        GPIO.output(13,(count & (1 << 1) == 2))
        GPIO.output(15,(count & (1 << 2) == 4))

def ledbulb_minus(channel):
        global count
        count = count - 1
        GPIO.output(11,(count & (1 << 0) == 1))
        GPIO.output(13,(count & (1 << 1) == 2))
        GPIO.output(15,(count & (1 << 2) == 4))

GPIO.add_event_detect(16,GPIO.RISING, callback=ledbulb_plus, bouncetime=200)

GPIO.add_event_detect(18,GPIO.RISING, callback= ledbulb_minus, bouncetime = 200)

while ((time.time()-begin) < 150):
        time.sleep(0.1)

GPIO.cleanup()
print (time.time()- begin)
