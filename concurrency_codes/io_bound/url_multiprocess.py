"""
- 멀티 프로세스를 이용해서 URL 요청하는 예제
- 여러 프로세스를 사용해서 I/O bound를 처리할 수 있지만.... Context Switch관점에서 리소스 소모가 쓰레드보다 더 크다.
"""
import multiprocessing
import requests
import time

session = None


# CPU 하나당 하나의 session만 갖을 수 있도록 한다.
def set_global_session():
    global session
    if not session:
        session = requests.Session()


def request_url(url):
    with session.get(url) as res:
        indicator = 'I' if 'ipython' in url else 'J'
        print(multiprocessing.current_process().name[-1], sep='', end='') # 현재 프로세스 넘버
        print(indicator, sep='', end='')


def request_all_urls(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(request_url, urls)
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
4I2I1I6I7I8I3I5I4J1J2J7J8J3J6J5J4I1I4J7I8I6I2I1J3I8J7J6J2J5I3J5J4I1I8I4J1J7I8J7J
Request 40 urls : 1.9372361910000002 sec.

40번의 URL 요청이 여러 프로세스를 통해 진행된다.
"""