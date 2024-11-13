# Download and load the spaCy language model
!python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')

# Define data fields
TEXT = data.Field(include_lengths=True)
LABEL = data.LabelField(dtype=torch.float)

# Load the IMDB dataset using torchtext.datasets
from torchtext.datasets import IMDB
train_data, test_data = IMDB.splits(TEXT, LABEL)
