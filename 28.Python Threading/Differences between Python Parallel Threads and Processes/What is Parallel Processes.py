from multiprocessing import Process

def GFG():
    for i in range(5):
        print(i)
# Create multiple processes
processes = []
for _ in range(3):
    process = Process(target=GFG)
    processes.append(process)
    process.start()
# Wait for all processes to complete
for process in processes:
    process.join()
