from multiprocessing import Process


def GFG(start, end):

    # Perform computation or task within the loop
    print(f"Processing range ({start}, {end})")


def parallel_while_loop():

    # Define the range of iterations for the loop
    start = 0
    end = 5

    # Create a separate process for the each iteration
    processes = []
    for i in range(start, end):
        process = Process(target=GFG, args=(i, i+1))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()


if __name__ == "__main__":
    parallel_while_loop()
