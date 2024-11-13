import threading


class counter_share:
    # multiple threads can share counter objects
    _lock = threading.RLock()

    def __init__(self, initial_key=0):
        self._key = initial_key

    def incr(self, delta=1):
        # Increasing the counter with lock
        with SharedCounter._lock:
            self._key += delta

    def decr(self, delta=1):
        # Decreasing the counter with lock
        with SharedCounter._lock:
            self.incr(-delta)
