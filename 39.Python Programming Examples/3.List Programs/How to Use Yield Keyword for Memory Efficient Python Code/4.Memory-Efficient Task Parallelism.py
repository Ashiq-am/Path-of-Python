def parallel_tasks():
    yield lambda x: x * 2
    yield lambda x: x ** 2
    # Add more tasks as needed

# Using the generator for parallel tasks
tasks_gen = parallel_tasks()
data = 5

for task in tasks_gen:
    result = task(data)
    print(result)
