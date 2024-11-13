# importing random module
import random
import mss

# importing time module
import time

# Running the while loop for infinite time
while True:
	# generating a random number between 1
	# to 5 , which will represent the time
	# delay
	random_time = random.randint(1, 5)

	# create a time delay using the sleep()
	# method
	time.sleep(random_time)

	# Save the screenshot shot using current time
	# as file name.
	file_name = str(time.time())+".png"

	# Take the screenshot using shot() method
	with mss.mss() as mss_obj:
		mss_obj.shot(output=file_name)
