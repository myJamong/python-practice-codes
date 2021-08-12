import time


def elapsed(func_to_time):
    def timed(*args, **kwargs):
        start = time.perf_counter()
        res = func_to_time(*args,  **kwargs)
        print('{:.5f} sec'.format(time.perf_counter() - start))
        return res
    return timed
