import torch
import multiprocessing as mp

if __name__ == '__main__':
    mp.set_start_method('spawn')  # or 'forkserver',
    loader = DataLoader(dataset, num_workers=4)
    for data in loader:
        # process data
