import time
import RPi.GPIO as GPIO

begin = time.time() #setting the timmer for running program for a certain tiome

#configuring GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0b000 # counter variable

""" 
function for incrementing the count value and
putting on the led to dispaly equivalent binary
value of count. Called by interrupt when swith at GPIO 16 is pressed
"""
def ledbulb_plus(channel):
	global count
	count = count +1
        GPIO.output(11,(count & (1 << 0) == 1)) #(Count & (1<<0)) bit filtering
        GPIO.output(13,(count & (1 << 1) == 2))
        GPIO.output(15,(count & (1 << 2) == 4)) 


""" 
function for decrementing the count value and
putting on the led to equivalent binary value of the count varieble
Called by interrupt when switch at GPIO pin 18 is pressed.
"""
def ledbulb_minus(channel):
        global count
        count = count - 1
        GPIO.output(11,(count & (1 << 0) == 1))
        GPIO.output(13,(count & (1 << 1) == 2))
        GPIO.output(15,(count & (1 << 2) == 4))

#interupts using rising edge on GPIO and also setting debounce for the buttons
GPIO.add_event_detect(16,GPIO.RISING, callback=ledbulb_plus, bouncetime=200)
GPIO.add_event_detect(18,GPIO.RISING, callback= ledbulb_minus, bouncetime = 200)

# to wait for a button press by polling loop. the looping time is 3 min
while ((time.time()-begin) < 150):
        time.sleep(0.1) # wait for 0.1s  to give cpu some rest

GPIO.cleanup() # clearing the GPIO pins
print (time.time()- begin)
