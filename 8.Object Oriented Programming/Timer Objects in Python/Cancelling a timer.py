#Syntax:

# timer.cancel()

# Stop the timer, and cancel the execution of the timer’s action. This will only work if the timer is still in its waiting stage.




# Program to cancel the timer
import threading

def gfg():
	print("GeeksforGeeks\n")

timer = threading.Timer(5.0, gfg)
timer.start()
print("Cancelling timer\n")
timer.cancel()
print("Exit\n")



