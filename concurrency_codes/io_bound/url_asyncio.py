"""
- coroutine을 이용한 비동기 URL 요청하는 예제
- 프로세스 하나, 쓰레드하나를 사용하지만... 제어권을 넘겨주면서 협력형 멀티태스킹으로 작업한다.
"""
import asyncio
import time

import aiohttp


# 비동기적으로 함수를 처리하겠다는 Keyword
async def request_url(session, url):
    async with session.get(url, ssl=False) as res:
        indicator = 'I' if 'ipython' in url else 'J'
        print(indicator, sep='', end='')


# 비동기적으로 함수를 처리하겠다는 Keyword
async def request_all_urls(urls):
    async with aiohttp.ClientSession() as session:
        # 실행에 대한 제어권을 넘겨줄 수 있다는 의미로 await 키워드 사용
        await asyncio.gather(*(request_url(session, url) for url in urls))
    print()


if __name__ == "__main__":
    urls = [
               "https://ipython.org/",
               'https://www.python.org/',
           ] * 80

    print('Start requests')
    start = time.perf_counter()
    """
    # Python 3.6 and before
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request_all_urls(urls))
    """

    # Python 3.7 and after
    asyncio.run(request_all_urls(urls))
    print('Request {} urls : {} sec.'.format(len(urls), time.perf_counter() - start))

"""
결과
Start requests
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJIIIIIIIIIIIIIIIIIIIIIIIIIJIIIIIJIJIIIIIIIIIJIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
Request 160 urls : 1.7996896640000002 sec.

160번의 URL 요청이 하나의 프로세스와 하나의 쓰레드에서 제어권을 넘겨주면서 요청하고 기다린다. 
"""