from pycaret.datasets import get_data
from pycaret.classification import setup
# Load dataset
data = get_data('juice')
# Initialize setup
clf1 = setup(data, target='Purchase')
