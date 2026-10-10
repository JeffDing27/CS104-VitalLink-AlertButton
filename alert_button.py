import requests
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed:
            print("Someone pressed the alert button!")
            button_pressed = True

            response = requests.post(f"https://api.telegram.org/bot8171305920:AAG4b8qFwvBPaOrt4XX7XZVpea_Rmh2z7sU/SendMessage",
             json={"chat_id": 8868443529, "text": "Someone pressed the alert button!"})
            print(response.json())
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()
