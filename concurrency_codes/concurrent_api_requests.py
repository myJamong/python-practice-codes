import asyncio
import time

import aiohttp


async def number_fact_request(num, session):
    """
    비동기적으로 동시에 API에 요청하기 위한 함수
    해당 예제는 숫자에 대한 정보를 알려주는 알려주는 API에 요청한다.
    """
    url = 'http://numbersapi.com/{}/math'.format(num)
    res = await session.request('GET', url)
    value = await res.text()
    return value


async def single_request():
    """
    비동기 요청에 대한 비교를 위한 함수 - 단일 요청
    """
    async with aiohttp.ClientSession() as session:
        res = await number_fact_request(3, session) # 비동기지만 1번 요청한다.
        print(res)


async def multi_request():
    """
    비동기 요청에 대한 비교를 위한 함수 - 다중 요청
    Python의 관점에서 1 프로세스, 1 쓰레드 단위로 실행이 되고 있지만...
    외부에서 병렬적으로 실행되고 있다.

    Python이 request의 제어권을 OS에 넘겨주므로 OS가 병렬적으로 작업한다.
    Python에서는 Event Loop을 통해서 제어권을 넘기고 결과에 받아서 Callback한다.
    그래서 제어권이 넘어간 순간부터 외부에서 알아서 원하는 방식으로 처리한다.
    """
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(number_fact_request(i, session) for i in range(1, 30))) # 비동기적으로 30번 요청한다.
        print(results)


if __name__ == "__main__":
    # API에 한번만 요청하여 걸리는 시간을 확인한다.
    start = time.perf_counter()
    asyncio.run(single_request())
    print('elapsed time : {:0.5f}s'.format(time.perf_counter() - start))

    # API에 여러번 요청하여 걸리는 시간을 확인한다.
    start = time.perf_counter()
    asyncio.run(multi_request())
    print('elapsed time : {:0.5f}s'.format(time.perf_counter() - start))
    # 비동기적으로 실행되어 큰 차이가 없다.
