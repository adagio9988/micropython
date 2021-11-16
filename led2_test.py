import machine
import time
import micropython
import network
import esp
#-------------------------

pin2 = machine.Pin(2,machine.Pin.OUT)

print(pin2.value())

while True:
    pin2.value(1)
    time.sleep(0.3)
    pin2.value(0)
    time.sleep(0.3)
    
    
