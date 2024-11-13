import time

def custom_keyboard_interrupt_handler():
    print("Custom KeyboardInterrupt caught! Cleaning up...")

try:
    print("Press Ctrl+C to interrupt")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    custom_keyboard_interrupt_handler()
print("Program terminated.")
