# Example code triggering the error on Python 3.9 or later
from collections import X

def process_data(data):
    # Your code here to process the data
    pass

if __name__ == "__main__":
    sample_data = {"key": "value"}
    process_data(sample_data)