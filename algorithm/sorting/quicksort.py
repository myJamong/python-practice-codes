# 피봇값을 정해서 3가지 영역으로 분리한다. 피봇보다 적은 값, 같은 값, 높은 값
# 이거를 재귀적으로 수행하고 리스트를 합친다.
# 병합정렬이랑 비슷하지만... 다른 것은 위치가 아닌 값으로 구분을 한다는 것.
# 정말 빠르지만 Stable하지 않다.
# 시간 복잡도 : nlog(n)
# 100,000건 : 0.09099 sec
import time
import random


def quicksort(items):
    if len(items) <= 1:
        return items
    #pivot = items[0]
    pivot = random.choice(items)
    less = [x for x in items if x < pivot]
    equals = [x for x in items if x == pivot]
    greater = [x for x in items if x > pivot]
    # 최악의 시간 복잡도는 n^2이다.
    # 만약 이미 정렬되어 있는 리스트에서 작업을 하게되면 하나 빼고 나머지값이 모두 less나 greater에 속해있어 필요없는 작업을 진행한다.
    # 그래서 피봇이 가장 낮은 값이나 가장 큰 값인 경우가 문제가 되는건데... 이런거를 해결하기 위해서 피봇값을 랜덤하게 받아오는게 좋다.
    return quicksort(less) + equals + quicksort(greater)

start = time.perf_counter()
# maximum recursion 오류가 발생할 수 있다.
# items = [_ for _ in range(50000)]
# 이 경우 피봇을 잘 정해야한다.

items = [random.randint(1, 1000) for _ in range(100000)]
print('{:.5f} sec'.format(time.perf_counter() - start))
print(len(quicksort(items)))
