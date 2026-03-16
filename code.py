import RPi.GPIO as GPIO
import time

# GPIO pin setup
PIR_PIN = 17
LED_PIN = 23
BUZZER_PIN = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

print("System Ready... Waiting for visitor")

try:
    while True:
        motion = GPIO.input(PIR_PIN)

        if motion == 1:
            print("Visitor Detected!")

            GPIO.output(LED_PIN, True)
            GPIO.output(BUZZER_PIN, True)

            time.sleep(3)

            GPIO.output(LED_PIN, False)
            GPIO.output(BUZZER_PIN, False)

            time.sleep(2)

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program Stopped")
    GPIO.cleanup()
