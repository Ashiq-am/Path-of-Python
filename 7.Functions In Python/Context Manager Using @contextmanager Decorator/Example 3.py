# Python program for creating a
# context manager using @contextmanager
# decorator

from contextlib import contextmanager


@contextmanager
def ContextManager():
    # Before yield as the enter method
    print("Enter method called")
    yield

    # After yield as the exit method
    print("Exit method called")


with ContextManager() as manager:
    print('with statement block')
