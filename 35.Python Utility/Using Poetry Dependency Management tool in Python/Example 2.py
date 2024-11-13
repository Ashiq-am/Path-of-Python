from plyer import notification
import time


def inputtime():
    hour = int(input("hours of interval :"))
    minutes = int(input("Mins of interval :"))
    seconds = int(input("Secs of interval :"))
    time_interval = seconds + (minutes * 60) + (hour * 3600)
    return time_interval


def notify():
    notification.notify(
        title="Time is Up",
        message="Enter description here",

        timeout=5
    )


if __name__ == '__main__':
    time_interval = inputtime()
    time.sleep(time_interval)
    notify()
