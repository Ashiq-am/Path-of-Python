# Example code triggering the error on
# an outdated Python version
from collections import X

def process_data(data):
    # Your code here to process the data
    pass

if __name__ == "__main__":
    sample_data = {"key": "value"}
    process_data(sample_data)