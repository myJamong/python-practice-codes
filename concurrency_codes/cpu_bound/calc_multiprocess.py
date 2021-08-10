"""
- 오래 걸리는 연산처리를 멀티 프로세스를 이용해서 비동기적으로 진행한다.
- 연산이 오래걸리는 작업을 여러 CPU를 사용해서 병렬적으로 연산을 수행한다.
"""
import multiprocessing
import time


def calc(top):
    return sum([i + j for i in range(top) for j in range(top)])


def calc_all(nums):
    with multiprocessing.Pool() as pool:
        pool.map(calc, nums)


if __name__ == '__main__':
    print('Start requests')
    start = time.perf_counter()
    calc_all([3000 + x for x in range(10)])
    print('Calc : {} sec.'.format(time.perf_counter() - start))

"""
결과
Start requests
Calc : 4.32297671 sec.

멀티 프로세스의 경우 여러 CPU를 사용해서 연산을 병렬적으로 진행하여
쓰레드나 동기적으로 연산했을 때보다 비교적 빠른 연산이 가능하다.
"""