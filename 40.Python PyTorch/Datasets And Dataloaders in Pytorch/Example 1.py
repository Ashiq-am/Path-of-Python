# importing libraries
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math


# class to represent dataset
class HeartDataSet():

    def __init__(self):
        # loading the csv file from the folder path
        data1 = np.loadtxt('heart.csv', delimiter=',',
                           dtype=np.float32, skiprows=1)

        # here the 13th column is class label and rest
        # are features
        self.x = torch.from_numpy(data1[:, :13])
        self.y = torch.from_numpy(data1[:, [13]])
        self.n_samples = data1.shape[0]

    # support indexing such that dataset[i] can
    # be used to get i-th sample
    def __getitem__(self, index):
        return self.x[index], self.y[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples


dataset = HeartDataSet()

# get the first sample and unpack
first_data = dataset[0]
features, labels = first_data
print(features, labels)
