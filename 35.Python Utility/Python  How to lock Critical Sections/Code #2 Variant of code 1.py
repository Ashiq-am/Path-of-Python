import threading


class counter_share:
    # multiple threads can share counter objects
    def __init__(self, initial_key=0):
        self._key = initial_key
        self._key_lock = threading.Lock()

    def incr(self, delta=1):
        # Increasing the counter with lock
        self._key_lock.acquire()
        self._key += delta
        self._key_lock.release()

    def decr(self, delta=1):
        # Decreasing the counter with lock
        self._key_lock.acquire()
        self._key -= delta
        self._key_lock.release()
