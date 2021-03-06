import pytest

from extra.lists.deque import Deque


def test_creating_deque(helper):
    # empty stack
    dq = Deque()
    assert dq._max_capacity == float("inf")
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() is None
    with pytest.warns(UserWarning):
        assert dq.pop_left() is None
    with pytest.warns(UserWarning):
        assert dq.pop_right() is None
    with pytest.raises(IndexError):
        dq.get_left()
    with pytest.raises(IndexError):
        dq.get_right()
    dq.clear()  # not to through any errors
    assert dq._max_capacity == float("inf")
    assert not dq.is_full()

    # empty stack with max_capacity == 0
    dq = Deque(max_capacity=0)
    assert dq._max_capacity == 0
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() is None
    with pytest.warns(UserWarning):
        assert dq.pop_left() is None
    with pytest.warns(UserWarning):
        assert dq.pop_right() is None
    with pytest.raises(IndexError):
        dq.get_left()
    with pytest.raises(IndexError):
        dq.get_right()
    with pytest.warns(UserWarning):
        dq.enqueue(helper.get_value())
    with pytest.warns(UserWarning):
        dq.append_left(helper.get_value())
    with pytest.warns(UserWarning):
        dq.append_right(helper.get_value())
    dq.clear()  # not to through any errors
    assert dq._max_capacity == 0
    assert dq.is_full()


def test_deque_with_max_capacity(helper):
    cap = helper.get_pos_int()
    # test append_left/pop_left
    lst = helper.get_list(length=cap)
    dq = Deque(max_capacity=cap)
    assert dq._max_capacity == cap
    for i in lst:
        dq.append_left(i)
    assert len(dq) == cap
    assert not dq.is_empty()
    assert dq.is_full()
    for _ in range(cap):
        assert dq.get_left() == lst[-1]
        assert dq.get_right() == lst[0]
        assert dq.pop_left() == lst.pop()
    assert len(dq) == 0
    assert dq.is_empty()
    assert dq.is_full() is False
    dq.enqueue(helper.get_value())
    # test max capacity after clear
    dq.clear()
    assert dq._max_capacity == cap

    # test append_right/pop_right
    lst = helper.get_list(length=cap)
    dq = Deque(max_capacity=cap)
    assert dq._max_capacity == cap
    for i in lst:
        dq.append_right(i)
    assert len(dq) == cap
    assert not dq.is_empty()
    assert dq.is_full()
    for _ in range(cap):
        assert dq.get_left() == lst[0]
        assert dq.get_right() == lst[-1]
        assert dq.pop_right() == lst.pop()
    assert len(dq) == 0
    assert dq.is_empty()
    assert dq.is_full() is False
    dq.enqueue(helper.get_value())
    # test max capacity after clear
    dq.clear()
    assert dq._max_capacity == cap


def test_deque_with_invalid_max_capacity(helper):
    with pytest.raises(TypeError):
        Deque(max_capacity=helper.get_list())
    with pytest.raises(TypeError):
        Deque(max_capacity=helper.get_string())
    with pytest.raises(ValueError):
        Deque(max_capacity=helper.get_neg_int())
    with pytest.raises(ValueError):
        Deque(max_capacity=helper.get_neg_float())


def test_creating_deque_with_random_numbers(helper):
    # stack with random values
    lst = helper.get_list(length=100)
    dq = Deque()
    for i in lst:
        dq.append_right(i)
    assert len(dq) == len(lst)
    assert dq.get_left() == lst[0]
    assert not dq.is_empty()
    assert not dq.is_full()
    for _ in range(len(lst)):
        assert dq.get_left() == lst[0]
        assert dq.dequeue() == lst.pop()
    assert len(dq) == 0
    assert dq.is_empty()
    with pytest.warns(UserWarning):
        assert dq.dequeue() is None
    assert dq.is_full() is False


def test_deque_with_known_values():
    # test using dequeue() / enqueue()
    dq = Deque(max_capacity=3)
    dq.enqueue(2)
    dq.enqueue(40)
    dq.enqueue(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.enqueue(16000)
    assert dq.get_left() == 16000
    assert dq.dequeue() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq._max_capacity == 3
    assert dq.is_full() is False
    # test using append_right() / pop_left()
    dq = Deque(max_capacity=3)
    dq.append_right(2)
    dq.append_right(40)
    dq.append_right(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.append_right(16000)
    assert dq.get_left() == 40
    assert dq.pop_left() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq._max_capacity == 3
    assert dq.is_full() is False
    # test using append_left() / pop_right()
    dq = Deque(max_capacity=3)
    dq.append_left(2)
    dq.append_left(40)
    dq.append_left(800)
    assert len(dq) == 3
    with pytest.warns(UserWarning):
        dq.append_left(16000)
    assert dq.get_right() == 40
    assert dq.pop_right() == 40
    assert not dq.is_empty()
    assert not dq.is_full()
    dq.clear()
    assert dq.is_empty()
    assert dq._max_capacity == 3
    assert dq.is_full() is False


def test_append_methods(helper):
    dq = Deque()
    with pytest.raises(ValueError):
        dq.enqueue(None)
    with pytest.raises(ValueError):
        dq.append_left(None)
    with pytest.raises(ValueError):
        dq.append_right(None)
    dq.enqueue("")
    dq.append_left("")
    dq.append_right("")
    dq.enqueue(helper.get_value())
    dq.enqueue(helper.get_int())
    dq.enqueue(helper.get_string())
    dq.enqueue(helper.get_float())
    dq.enqueue(helper.get_list())
