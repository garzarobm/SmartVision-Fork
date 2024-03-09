
try:
    while True:
        # Move the servo back and forth between 0 and 180 degrees
        for duty_cycle in range(0, 10, 1):
            servo.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)
        for duty_cycle in range(10, 0, -1):
            servo.ChangeDutyCycle(duty_cycle)
            time.sleep(0.5)
except KeyboardInterrupt:
    # Clean up the GPIO on interrupt
    servo.stop()
    GPIO.cleanup()
    
#instructions to run larger servo
#1. Connect the servo to the raspberry pi
#2. Run the code
#3. The servo should move back and forth
#4. Press Ctrl+C to stop the code


# for serial communication
# Path: hardware_setup/serial_test.py
import serial
import time

# Set up the serial port
ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    while True:
        # Send a message to the Arduino
        ser.write(b'Hello, Arduino!')
        time.sleep(1)
        # Read a message from the Arduino
        print(ser.readline())   
except KeyboardInterrupt:
    # Close the serial port on interrupt
    ser.close()

#instructions to run serial communication
#1. Connect the arduino to the raspberry pi
#2. Run the code
#3. The code should send a message to the arduino and receive a message from the arduino
#4. Press Ctrl+C to stop the code
