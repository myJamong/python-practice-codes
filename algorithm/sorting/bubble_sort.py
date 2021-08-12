# 리스트의 가장 뒤에서부터 정렬이 된다.
# 리스트의 처음부터 시작해서 정렬되지 않는 부분까지 바로 뒤의 숫자와 비교해서 위치를 바꾼다.
# 느리다. 실절에서는 잘 사용 안한다. Stable
# 시간 복잡도 : n^2
# 5000건 : 2.27075 sec
from timing import elapsed
import random


@elapsed
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


items = [random.randint(1, 1000) for _ in range(5000)]
print(len(bubble_sort(items)))
