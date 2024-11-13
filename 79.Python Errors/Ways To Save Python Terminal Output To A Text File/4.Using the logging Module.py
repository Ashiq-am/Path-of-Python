import logging

# Configure logging to save to a file
logging.basicConfig(filename='output.log', level=logging.INFO)

for i in range(10):
	logging.info("printing line %d", i)
