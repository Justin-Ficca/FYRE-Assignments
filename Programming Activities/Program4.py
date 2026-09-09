# This program will turn on and off an arduino green led to make it blink

#incorperate the modules
import machine # module with microcontoller stuff
import time #module with time 


# assigning led to the first pin to use the green led light
#Green led is GPIO Pin 0
led = machine.Pin(0, machine.Pin.OUT)


while True:
  led.value(1) #turns on the LED
  time.sleep(.25) #pauses the loop for .25 seconds
  led.value =(0) #turns off the LED
  time.sleep(.25) #delay again
