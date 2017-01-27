import logging    
import RPi.GPIO as GPIO
import send_sms

#notify = imp.load_source('module.name', '/.py')

GPIO.cleanup() 

GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals  
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#setup logging
logging.basicConfig(filename='garage.log', level=logging.INFO)
logging.info('Garage Door Check Started')

# write door status changes
def writeStatus():
	#logging.info('writing current status')
        f = open ('garage.status','w')
        f.write(status)
        f.close
        return

def notify(statusVerbose):
	smsRecipient = 'your mobile here'
	smsInputMessage = statusVerbose
	send_sms.clickatelSMS(smsRecipient, smsInputMessage)
	return

def doorStartsOpen():
	print 'Door starts Open'
	var = 1
	while var == 1 :
    		GPIO.wait_for_edge(23, GPIO.FALLING)
        	statusVerbose = 'Garage has just Closed'
        	status = 'closed'
        	writeStatus()
        	print(statusVerbose)
        	logging.info(statusVerbose)
#        	notify(statusVerbose)
	
        	GPIO.wait_for_edge(23, GPIO.RISING)
        	statusVerbose = 'Garage has just Opened'
        	status = 'open'
        	writeStatus()
        	print(statusVerbose)
        	logging.info(statusVerbose)
#        	notify(statusVerbose)
	return(status,statusVerbose)

def doorStartsClosed():
	print 'Door starts Closed'
	var = 1
        while var == 1 :
                GPIO.wait_for_edge(23, GPIO.RISING)
                statusVerbose = 'Garage has just Opened'
                status = 'open'
                writeStatus()
                print(statusVerbose)
                logging.info(statusVerbose)
#                notify(statusVerbose)
        
                GPIO.wait_for_edge(23, GPIO.FALLING)
                statusVerbose = 'Garage has just Closed'
                status = 'closed'
                writeStatus()
                print(statusVerbose)
                logging.info(statusVerbose)
#                notify(statusVerbose)
	return(status,statusVerbose)

#Check and write current status of door
GPIO.input(23)
print GPIO.input(23)

if GPIO.input(23):
    statusVerbose = 'Garage is currently Open'
    status = 'open'
    writeStatus()
    print(statusVerbose)
    logging.info(statusVerbose)
    notify(statusVerbose)
    doorStartsOpen()
else:
    statusVerbose = 'Garage is currently Closed'
    status = 'closed'
    writeStatus()
    print(statusVerbose)
    logging.info(statusVerbose)
    notify(statusVerbose)
    doorStartsClosed()

print 'Waiting for status change'

# BASIC DOOR CHECK
#run interrupt 'while' to track door status changes
#var = 1 
#while var == 1 :
#	GPIO.wait_for_edge(23, GPIO.RISING)
#	statusVerbose = 'Garage has just Opened'
#    	status = 'open'
#    	writeStatus()
#    	print(statusVerbose)
#    	logging.info(statusVerbose)
#	notify(statusVerbose)
#
#	GPIO.wait_for_edge(23, GPIO.FALLING)
#	statusVerbose = 'Garage has just Closed'
#        status = 'closed'
#        writeStatus()
#        print(statusVerbose)
#        logging.info(statusVerbose)
#	notify(statusVerbose)

GPIO.cleanup()           # clean up GPIO on normal exit  

