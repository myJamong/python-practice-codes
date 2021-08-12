# 두번째 요소부터 시작해서 가장 앞에서부터 확인 및 비교하여 해당 위치로 삽입한다.
# 여전히 느리다. 버블정렬보다 상황별로 속도가 좀 더 빠르다. Stable
# 시간 복잡도 : n^2
# 5000건 : 1.29315 sec
from timing import elapsed
import random


@elapsed
def insertion_sort(items):
    for i in range(1, len(items)):
        curr_item = items[i]
        j = i - 1
        while j >= 0 and curr_item < items[j]:
            # 버블정렬에서는 자리를 교환하느라 두가지 연산을 했다면..
            # 삽입정렬에서는 한가지 연산만 진행하므로 시간 복잡도는 같지만 비교적 빠르다.
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = curr_item
    return items


items = [random.randint(1, 1000) for _ in range(5000)]
print(len(insertion_sort(items)))
