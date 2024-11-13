# Main function to initialize the processes
def main():
    world_size = 2
    mp.spawn(train, args=(world_size,), nprocs=world_size, join=True)

if __name__ == "__main__":
    main()
