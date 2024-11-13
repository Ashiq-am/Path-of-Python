import schedule
import time

# Define a function to print a message


def print_message():
    print("Hello! It's time to code on GFG")


# Schedule the task to run every day at 7:00 AM
schedule.every().day.at("10:35").do(print_message)

while True:
    schedule.run_pending()
    time.sleep(1)