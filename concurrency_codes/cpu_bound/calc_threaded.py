"""
- 오래 걸리는 연산처리를 쓰레드를 이용해서 비동기적으로 진행한다.
- 연산이 오래걸리는 작업이라 쓰레드를 늘린다고 해결할 수 있는 문제가 아니다.
"""
from concurrent import futures
import time


def calc(top):
    return sum([i + j for i in range(top) for j in range(top)])


def calc_all(nums):
    with futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(calc, nums)


if __name__ == '__main__':
    print('Start requests')
    start = time.perf_counter()
    calc_all([3000 + x for x in range(10)])
    print('Calc : {} sec.'.format(time.perf_counter() - start))

"""
결과
Start requests
Calc : 11.306376006 sec.

멀티 프로세스의 경우 여러 CPU를 사용해서 연산을 병렬적으로 진행하는데
멀티 쓰레드의 경우 같은 프로세스내에서 업무를 분할해서 하다보니... 연산 자체에 대한 속도를 개선할 수 없다.
"""