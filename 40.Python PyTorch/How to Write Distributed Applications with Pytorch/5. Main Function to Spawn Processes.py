def main():
    size = 2  # Number of processes
    mp.spawn(train, args=(size,), nprocs=size, join=True)
