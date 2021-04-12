#!/usr/bin/env python3

from threading import Semaphore


class ConcurrentQueue(object):
    """ Primitive Queue object
    """

    def __init__(self, capacity=4096):
        self.data = []

        # Inverted semaphore >:3
        self.available = Semaphore(capacity)
        [self.available.acquire() for _ in range(capacity)]

    def put(self, item):
        self.available.release()
        self.data += [item]

    def get(self):
        self.available.acquire()
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0
