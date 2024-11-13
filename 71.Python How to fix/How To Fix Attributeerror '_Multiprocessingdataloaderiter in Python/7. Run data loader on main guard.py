if __name__ == '__main__':
    loader = DataLoader(dataset, num_workers=4)
    for data in loader:
        # process data
