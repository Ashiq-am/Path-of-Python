import time
from collections import deque


# LRU cache implementation
class LRUCache:

    def __init__(self, size=5):
        self.size = size
        self.container = deque()
        self.map = dict()

    def reallocate(self):
        # to reallocate the hashmap for
        # every access of file access file
        # will reallocate the data in hashmap
        # according to the numbers position
        # in the container for every access,
        # hit and miss(evict)
        if len(self.container) > 1:

            for key, val in enumerate(self.container):
                self.map[val] = key

    def access(self, val):

        # print("access "+str(val))
        self.container.remove(val)
        self.container.appendleft(val)
        self.reallocate()

    def evict(self, val):

        # print("cache miss "+str(val))
        if val in self.map:
            # del self.map[val]
            self.container.remove(val)

        else:
            x = self.container.pop()
            del self.map[x]

        self.normal_insert(val)

    def normal_insert(self, val):
        self.container.appendleft(val)
        self.reallocate()

    def insert(self, val):

        if val in self.map.keys():

            # if vlaue in present in
            # the hashmap then it is a hit.
            # access function will access the
            # number already present and replace
            # it to leftmost position
            self.access(val)

        else:
            # if value is not present in
            # the hashtable
            if (len(self.map.keys()) == self.size):
                # if the size of the queue
                # is equal to capacity and
                # we try to insert the number,
                # then it is a miss then,
                # evict function will delete the
                # right most elements and insert
                # the latest element in the
                # leftmost position
                self.evict(val)

            else:
                # normal_insert function will normally
                # insert the data into the cache..
                self.normal_insert(val)

    def print(self):
        lru_elements = [x for x in self.container]
        print(lru_elements)


# definition of lru decorator
def LRUDecorator(size):
    lru = LRUCache(size)

    def decorator(function):
        def functionality(num):
            lru.insert(num)
            lru.print()

            # to check the num pageframe(position)
            # uncomment the below statement
            # print(lur.map)
            print(num, function(num))

        return functionality

    return decorator


# Using LRU Decorator
@LRUDecorator(size=4)
def ex_func_01(n):
    print(f'Computing...{n}')
    time.sleep(1)
    return n


print(f'\nFunction: ex_func_01')
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(5))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(5))
