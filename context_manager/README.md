# Context Managers
Context managers allow you to allocate and release resources precisely when you want to.

Context Manager를 사용하면 외부 리소스를 처리할 때 안전하게 리소스를 다시 반환하는 프로그래밍이 가능하다. 원하는 타이밍에 정확하게 리소스를 할당 및 제공 또는 반환하는 역할을 하고 with 구문과 함께 사용된다.
외부에서 Connection을 연결하고 제때 반환시키거나... 파일을 Open하고 Close하는 역할을 제어할 수 있다.

refference : https://book.pythontips.com/en/latest/context_managers.html