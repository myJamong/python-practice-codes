# Concurrency
- 병행성(Concurrency), 병렬성(Parallelism) 모두 여러 작업을 동시에하는 것이다.
- 많은 연산 작업은 I/O-bound의 작업이다.
   - disk나 network를 기다린다는 뜻. -> 연산하는 시간보다 기다리는 시간이 더 길어질 수 있다는 것.
   - OS는 제어권을 갖고 멀티 태스킹
- multi-processor

### Python concurrency libraries
- threading (I/O-bound)
- asyncio (I/O-bound)
- multiprocessing (multiprocessor problems)

### Concurrency Problems in Python
- GIL(Global Interpreter Lock)
    - 한번에 하나의 작업만할 수 있도록 하는 Python의 locking mechanism
    - Mutex(thread lock) ensuring only one thread controls the interpreter at a time
    - Limits multi-threaded execution
    - In place to prevent race conditions with memory and reference allocation
    - Particularly important when Python interacts with C-extensions
    - Lots of discussions on what to do about the GIL
        - Guido: only remove GIL if new code does not decrease the performance of a single-threaded program
        - Cpython and PyPy thing! Jython and IronPython do not use GIL
    
# asyncio
asyncio는 async/await 문법을 사용해서 병행성 코드(concurrent code)를 작성할 수 있고 IO bound application에서 주로 사용하는 라이브러리이다.

application이 느리고, 느린 이유가 잦은 I/O로 인한 경우라면... asyncio로 성능을 확실히 개선할 수 있다.

---

아래와 같은 상황에서 사용될 수 있다.

- API 요청과 같이 HTTP/HTTPS 통신
- 데이터베이스 통신
- 파일 시스템 I/O

Python의 프로그램 내부가 아닌... 외부의 통신에 있어서 속도가 느린 경우 사용될 수 있다.