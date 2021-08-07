from decimal import Decimal
from time import perf_counter
from datetime import datetime
from contextlib import contextmanager

@contextmanager
def Timer(task_name):
    def get_time():
        return Decimal(perf_counter())

    try:
        start = get_time()
        yield datetime.now() # entry point for the with statement. --> '__enter__' functions return value as generator.
    except Exception as e:
        raise
    else: # works as exit point after yield keyword. --> '__exit__'
        print('----- {}: {:.5f}s -----\nend datetime: {}\n'.format(task_name, get_time() - start, datetime.now()))


if __name__ == "__main__":
    with Timer('Outer Task') as t:
        print('some tasks in outer started at {}'.format(t))
        for _ in range(10000000):
            pass
        with Timer('Inner Task') as t:
            print('some tasks in inner started at {}'.format(t))
            for i in range(10000000):
                pass
