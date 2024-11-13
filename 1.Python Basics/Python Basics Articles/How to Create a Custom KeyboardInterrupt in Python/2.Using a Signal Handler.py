import signal
import time

def custom_keyboard_interrupt_handler(signum, frame):
    print("Custom KeyboardInterrupt (Ctrl+C) caught! Cleaning up...")

# Register the custom signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, custom_keyboard_interrupt_handler)

try:
    print("Press Ctrl+C to interrupt")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Standard KeyboardInterrupt caught! Exiting...")
print("Program terminated.")
