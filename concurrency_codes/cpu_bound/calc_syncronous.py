"""
- 오래 걸리는 연산처리를 동기적으로 진행한다.
- 연산이 오래걸리는 작업으로 그냥 오래 걸린다.
"""
import time


def calc(top):
    return sum([i + j for i in range(top) for j in range(top)])


def calc_all(nums):
    for num in nums:
        calc(num)


if __name__ == '__main__':
    print('Start requests')
    start = time.perf_counter()
    calc_all([3000 + x for x in range(10)])
    print('Calc : {} sec.'.format(time.perf_counter() - start))

"""
결과
Start requests
Calc : 9.888230081 sec.

그냥 오래 걸리는 작업이다.
"""