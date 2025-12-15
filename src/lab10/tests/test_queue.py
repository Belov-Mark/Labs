import pytest

from src.lab10.src.structures import Queue


def test_queue_initially_empty():
    q = Queue()
    assert q.is_empty()
    assert len(q) == 0
    assert q.peek() is None


def test_queue_enqueue_dequeue_fifo():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert len(q) == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()


def test_queue_peek_does_not_remove():
    q = Queue()
    q.enqueue("x")
    assert q.peek() == "x"
    assert len(q) == 1


def test_queue_dequeue_empty_raises():
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
