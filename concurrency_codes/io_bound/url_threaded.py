"""
- 쓰레드릴 이용한 비동기 URL 요청하는 예제
- 동기적인 방법과 똑같이 요청에 대한 답변을 기다리지만... 여러 쓰레드가 같이 요청하고 기다리기에 비교적 빠르다.
"""
from concurrent import futures
import requests
import threading
import time

local_thread = threading.local()


def request_url(url):
    if not hasattr(local_thread, 'session'):
        local_thread.session = requests.Session()

    with local_thread.session.get(url) as res:
        indicator = 'I' if 'ipython' in url else 'J'
        print(indicator, sep='', end='')


def request_all_urls(urls):
    # 쓰레드의 수에 따라 속도가 달라진다.
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(request_url, urls)
    print()


if __name__ == "__main__":
    urls = [
               "https://ipython.org/",
               'https://www.python.org/',
           ] * 20

    print('Start requests')
    start = time.perf_counter()
    request_all_urls(urls)
    print('Request {} urls : {} sec.'.format(len(urls), time.perf_counter() - start))

"""
결과
Start requests
JJJJJJJJJIIIIIJJJJJIIIIJIIJJIJJIJIIIIIII
Request 40 urls : 1.2656733949999999 sec.

40번의 URL 요청이 여러 쓰레드로 나눠 진행되고 같이 기다린다.
요청이 끝나는대로 결과를 반환해줘서 작업이 순차적으로 진행되지 않는다.
여전히 연산하는 속도보다 요청하고 기다리는 시간의 비율이 크지만... 기다리는 시간이 쓰레드로 분산되어 빠르다. 
"""