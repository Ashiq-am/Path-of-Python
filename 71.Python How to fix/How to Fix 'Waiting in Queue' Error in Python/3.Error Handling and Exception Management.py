import logging

logging.basicConfig(level=logging.INFO)
def process_item(item):
    try:
        # Simulate processing
        if item % 5 == 0:
            raise ValueError('Simulated error')
        logging.info(f'Processed item: {item}')
    except Exception as e:
        logging.error(f'Error processing item {item}: {e}')
for item in range(20):
    process_item(item)
