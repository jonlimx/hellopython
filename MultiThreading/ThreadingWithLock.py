import threading


class ShareCounter(object):
    """
    A counter object that can be shared by multiple threads
    """
    def __init__(self, initial_value):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def increase(self, delta=1):
        """
        Increment the counter with locking
        :param delta: By default, we increase the value by 1
        :return:
        """
        with self._value_lock:
            self._value += delta

    def descrease(self, delta=1):
        """
        Decrement the counter with locking
        :param delta: By default, we decrease the value by 1
        :return:
        """
        with self._value_lock:
            self._value -= delta
