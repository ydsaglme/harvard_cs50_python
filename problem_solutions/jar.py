class Jar:
    def __init__(self, capacity = 12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self._size = self.size + n

    def withdraw(self, n):
        if 0 > self.size - n:
            raise ValueError
        else:
            self._size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size