from gpiozero import DigitalInputDevice, OutputDevice 
from time import sleep 
 
# GPIO pin settings 
ir = DigitalInputDevice(27) 
relay = OutputDevice(17, active_high=False, initial_value=False) 
 
print("IR Sensor + Relay System Started") 
 
try: 
    while True: 
        if ir.value == 0: 
            print("Object Detected! Relay ON") 
            relay.on() 
        else: 
            print("No Object! Relay OFF") 
            relay.off() 
 
        sleep(0.3) 
 
except KeyboardInterrupt: 
    relay.off() 
    print("\nProgram stopped. Relay OFF.")