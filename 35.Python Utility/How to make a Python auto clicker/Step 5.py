# method to check and run loop until
# it is true another loop will check
# if it is set to true or not,
# for mouse click it set to button
# and delay.
def run(self):
	while self.program_running:
		while self.running:
			mouse.click(self.button)
			time.sleep(self.delay)
		time.sleep(0.1)
