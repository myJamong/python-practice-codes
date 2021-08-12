# 리스트를 반으로 재귀적으로 쪼개서 --> 원소가 하나로 줄어들 때 까지
# 정렬하여 다시 합친다.
# 퀵정렬이랑 비슷하지만... 다른 것은 값이 아닌 위치로 구분을 한다는 것.
# 두개의 정렬된 리스트를 합치는데 시간 복잡도는 n이다.
# 빠르다, Stable
# 시간 복잡도 : nlog(n)
# 100,000건 : 0.08873 sec
import time
import random
import math


def merge_sorted_lists(left, right):
    left_idx, right_idx = 0, 0
    return_list = []

    while len(return_list) < len(left) + len(right):
        left_item = left[left_idx] if left_idx < len(left) else math.inf
        right_item = right[right_idx] if right_idx < len(right) else math.inf
        if left_item < right_item:
            return_list.append(left_item)
            left_idx += 1
        else:
            return_list.append(right_item)
            right_idx += 1
    return return_list


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left, right = items[:mid], items[mid:]
    return merge_sorted_lists(merge_sort(left), merge_sort(right))


start = time.perf_counter()
items = [random.randint(1, 1000) for _ in range(100000)]
print('{:.5f} sec'.format(time.perf_counter() - start))
print(len(merge_sort(items)))
