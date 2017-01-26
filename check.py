    
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# write door status changes
def writeStatus():
        f = open ('garage.status','w')
        f.write(status)
        f.close
        return

#Check and write current status of door
GPIO.input(23)

if GPIO.input(23):
    print('Garage is currently Open')
    status = 'open'
    writeStatus()
else:
    print('Garage is currently Closed')
    status = 'closed'
    writeStatus()

print 'Waiting for status change'
#run interrupt 'while' to track door status changes
var = 1 
while var == 1 :
	GPIO.wait_for_edge(23, GPIO.RISING)
	print "\nDoor Open"
	status = 'open'
	writeStatus()

	GPIO.wait_for_edge(23, GPIO.FALLING)
	print "\nDoor Closed"
	status = 'closed'
	writeStatus()

GPIO.cleanup()           # clean up GPIO on normal exit  

