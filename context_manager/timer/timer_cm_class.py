from decimal import Decimal
from time import perf_counter

class Timer():
    def __init__(self, task_name):
        self._task_name = task_name

    def __enter__(self): # entry point for the with statement.
        self._start = self.get_time()
        return self._start

    def __exit__(self, exc_type, exc_val, exc_tb): # exit point for the with statement.
        if exc_type:
            raise
        else:
            print('----- {}: {:.5f}s -----'.format(self._task_name, self.get_time() - self._start))
        return True

    def get_time(self):
        return(Decimal(perf_counter()))


if __name__ == "__main__":
    with Timer('Outer Task'):
        print('some tasks in outer')
        for _ in range(100000):
            pass
        with Timer('Inner Task'):
            print('some tasks in inner')
            for i in range(100000):
                pass