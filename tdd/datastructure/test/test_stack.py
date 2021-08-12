from stack.stack import Stack
import pytest


@pytest.fixture() # 코드의 재활용을 하기 위해 fixture 사용
def stack(): # 해당 메소드 이름으로 test 메소드에서 인자로 받을 수 있다.
    return Stack()


def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2


def test_pop(stack):
    stack.push('hello')
    stack.push('world')
    assert stack.pop() == 'world'
    assert stack.pop() == 'hello'
    assert stack.pop() is None
