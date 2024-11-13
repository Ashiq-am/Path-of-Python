# Python program to demonstrate
# threading module
import threading


def trace_function():
    print("Passing the trace function")


def profile():
    print("Setting the profile of thread: " + str(threading.current_thread().getName()))


class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        print(str(self.thread_ID))
        print("Number of active threads: " + str(threading.active_count()))
        print("Name of current thread: " + str(threading.current_thread().getName()))


thread1 = thread("GFG", 1000)
thread2 = thread("GeeksforGeeks", 2000)
print("Name of main thread: " + str(threading.main_thread().getName()))
print("Identity of main thread: " + str(threading.get_ident()))
print("Stack size = " + str(threading.stack_size()))
print(threading.settrace(trace_function()))
threading.setprofile(profile())

thread1.start()
thread2.start()
print("Enumeration list: ")
print(threading.enumerate())
print("Exit")
