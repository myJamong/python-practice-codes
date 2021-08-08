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
    
## Threading
- Most programs spend a lot of time waiting for I/O
- Threads allow you to time slice your computation, doing processing work while waiting
- Threads work within the GIL
- Significant speed-up can result for disk or network heavy software

## asyncio
asyncio는 async/await 문법을 사용해서 병행성 코드(concurrent code)를 작성할 수 있고 IO bound application에서 주로 사용하는 라이브러리이다.

application이 느리고, 느린 이유가 잦은 I/O로 인한 경우라면... asyncio로 성능을 확실히 개선할 수 있다.

Event loop와 coroutine을 사용하는데 Event loop는 Python 내부에 발생되는 작업에 대한 순서를 제어하는 메인 Loop가 있다.

---

아래와 같은 상황에서 사용될 수 있다.

- API 요청과 같이 HTTP/HTTPS 통신
- 데이터베이스 통신
- 파일 시스템 I/O

Python의 프로그램 내부가 아닌... 외부의 통신에 있어서 속도가 느린 경우 사용될 수 있다.

---
asyncio는 두가지 built-in keyword를 사용한다.
- async : indicates that code is to be run asynchronously
- await : the cooperative signal that your coroutine is willing to give up execution control.

asyncoc Library 주의 사항
- Python 3.4에서 소개되었다.
- asyncio still fairly new
- Libraries are just starting to take advantage of it
    - Instead of "requests", need "aiphttp"
  ---

## Thread vs asyncio
둘다 I/O-bound에 대한 처리를 위해 사용
- asyncio는 python에서 제어가 되고 동시성에 오버헤드가 비교적 적다.
- coding with asyncio is slightly more complicated
- asyncio is still new
- asyncio is Co-operative vs Threads are pre-emptive multitasking

Both the threading library and the asyncio library operate inside of a single Python interpreter, 
and therefore are encumbered by the GIL.
If you're doing I/O-bound concurrency, this typically isn't a problem.
You can still get speed-up because of the long latency waiting for network or disk access.


---
## Multiprocessing
The multiprocessing library gives ability to spin up an interpreter per CPU.
This allows you to do CPU-bound concurrency.
As each CPU gets its own instance of the interpreter, the GIL isn't a problem.
You get 1 GILL per CPU.


## Multiprocessing vs Threading
So if multiprocessing partially solves the GIL problem, why wouldn't you just do this all the time?
- It creates a log of overhead in creating a process
  - the implementation of a process happens at the OS level
    so you will also see behavior and scheduling differences between OS's in your code.
  - Each process gets its own copy of the interpreter, it tends to require more memory than threading does as well.
  - You have to spin up the interpreter so the initialization time of each process tends to be longer than threads.
  
Threads were introduced into operating systems as a lightweight way of getting around the overhead involved in processes.
Because each process has its own interpreter and does not share memory footprints,
communicating between the processes must be done with explicit constructs.
The multiprocessing library comes with a few that can help you do that.


threading and asyncio tend to be beneficial in I/O-bound situations.
They’re not beneficial in CPU-bound situations.
That’s where multiprocessing reigns.

---
## I/O bound vs CPU bound

- I/O bound : waiting on input and output
  - the vast majority of the time the program spends running is waiting for input and output
    - ex) Downloading content from the web
    - The amount of latency involved in network transactions far outweighs the computation involved in downloading it.
  
The threading and asyncio libraries only see speed-up in I/O bound cases,
because they are scheduling computation while the other threads are waiting for the I/O.
You get speed-up because you're not waiting for one piece of I/O at a time.
You're waiting for multiple pieces of I/O at a time.

지연에 대한 이점을 얻을 수 있다. I/O bound는 DB 연결이나 파일 읽고 쓰거나 네트워크 연결과 같이 외부적으로 통신이 필요한 경우에서
여러 연결이 발생할 때... 비동기적으로 진행시키면... 연결 하나씩 요청을 해놓고 기다리려야하니까... 
멀티 프로세싱이 아니라 멀티 쓰레딩이나 Python에서는 코루틴을 사용해서 해결할 수 있는 것이다.
굳이 여러 프로세스를 사용해서 작업할 필요가 없다는 것이다.


- CPU bound : waiting on computation

If your program instead is doing something that requires a lot of work inside of the CPU rather than waiting on a peripheral,
  then threading and asyncio is not going to give you that kind of improvement.
  you need multiple CPUs working simutaneously.
  the multiprocessing library does allow you to do this.

쓰레딩이나 코루틴으로 사용한 동시성과 달리 멀티 프로세싱을 사용하면... CPU 연산에 대한 속도 개선이 가능하다.
단순하게 계산이 오래 걸리는 문제를 해결하기 위해 Thread나 asyncio를 사용하면...
이 문제를 해결할 수 없지만.. 멀티 프로세싱을 통해 여러 CPU를 사용해서 연산하면 해결이 가능하다.
