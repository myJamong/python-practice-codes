from decimal import Decimal
from time import perf_counter
from datetime import  datetime

class Timer():
    def __init__(self, task_name):
        self._task_name = task_name

    def __enter__(self): # entry point for the with statement.
        self._start = self._get_time()
        return datetime.now() # returns value to use in with statement.

    def __exit__(self, exc_type, exc_val, exc_tb): # exit point for the with statement.
        if exc_type: # if exception
            raise
        else:
            print('----- {}: {:.5f}s -----\nend datetime: {}\n'.format(self._task_name, self._get_time() - self._start, datetime.now()))
        return True

    def _get_time(self):
        return Decimal(perf_counter())


if __name__ == "__main__":
    with Timer('Outer Task') as t:
        print('some tasks in outer started at {}'.format(t))
        for _ in range(10000000):
            pass
        with Timer('Inner Task') as t:
            print('some tasks in inner started at {}'.format(t))
            for i in range(10000000):
                pass
