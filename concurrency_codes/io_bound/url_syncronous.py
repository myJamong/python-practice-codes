"""
- 동기적으로 URL 요청하는 예제
- 순차적으로 결과를 받아오고 연산하는 속도보다 요청하고 기다리는 시간의 비율이 크다.
"""
import requests
import time


def request_url(url):
    session = requests.Session()
    with session.get(url) as res:
        indicator = 'I' if 'ipython' in url else 'J'
        print(indicator, sep='', end='')


def request_all_urls(urls):
    for url in urls:
        request_url(url)
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
IJIJIJIJIJIJIJIJIJIJIJIJIJIJIJIJIJIJIJIJ
Request 40 urls : 14.574426024 sec.

40번의 URL 요청이 순차적으로 진행되고 연산하는 속도보다 요청하고 기다리는 시간의 비율이 크다. 
"""