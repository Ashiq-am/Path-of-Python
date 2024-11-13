import torch
from torchtext import data
from torch.nn.utils.rnn import pad_sequence
from collections import Counter
import spacy
import torch.optim as optim
from torchtext.data import BucketIterator
from pprint import pprint  # Importing pprint for pretty-printing
