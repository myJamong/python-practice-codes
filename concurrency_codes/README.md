# asyncio
asyncio는 async/await 문법을 사용해서 병행성 코드(concurrent code)를 작성할 수 있고 IO bound application에서 주로 사용하는 라이브러리이다.

application이 느리고, 느린 이유가 잦은 I/O로 인한 경우라면... asyncio로 성능을 확실히 개선할 수 있다.

---

아래와 같은 상황에서 사용될 수 있다.

- API 요청과 같이 HTTP/HTTPS 통신
- 데이터베이스 통신
- 파일 시스템 I/O

Python의 프로그램 내부가 아닌... 외부의 통신에 있어서 속도가 느린 경우 사용될 수 있다.