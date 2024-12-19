import threading


def func1():
    print("Task One Started")


def func2():
    print("Task Two Started")


thread1 = threading.Thread(target=func1)
thread2 = threading.Thread(target=func2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()