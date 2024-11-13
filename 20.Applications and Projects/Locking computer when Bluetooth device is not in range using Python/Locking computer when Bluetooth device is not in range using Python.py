# Import required packages
import schedule
import time
import bluetooth
import ctypes


def job():
    # Find your bluetooth uuid in your
    # mobile and give set it in the
    # variable
    inputBdaddr = "XX:XX:XX:XX:XX:XX"

    # Variable to find whether the
    # given bluetooth uuid is
    # present in the discovered devices
    passed = False

    # Try to search for the nearby
    # visible devices
    try:
        # Get the list of discovered devices
        scan = bluetooth.discover_devices()

        # Search for your bluetooth uuid
        # in the scanned devices If found
        # set the variable to true else
        # set the variable to false
        if inputBdaddr in scan:
            passed = True

        else:
            passed = False

    except:
        passed = False

    # When bluetooth device
    # is not found, lock the
    # workstation
    if not passed:
        ctypes.windll.user32.LockWorkStation()

    # Schedule the process


# to run every 30 seconds
schedule.every(30).seconds.do(job)

# Check whether a scheduled
# task is pending to run or not
while 1:
    schedule.run_pending()
    time.sleep(1)
