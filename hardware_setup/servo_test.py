import RPi.GPIO as GPIO
import time

# Set the pin for the servo
servo_pin = 17

# Set up the GPIO library
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up the servo and start it
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency
servo.start(0)  # Initial duty cycle of 0

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