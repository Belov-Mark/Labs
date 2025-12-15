import pytest

from src.lab10.src.linked_list import SinglyLinkedList


def test_empty_list():
    lst = SinglyLinkedList()
    assert len(lst) == 0
    assert list(lst) == []
    assert lst.head is None
    assert lst.tail is None


def test_append():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    assert list(lst) == [1, 2, 3]
    assert len(lst) == 3
    assert lst.head.value == 1
    assert lst.tail.value == 3


def test_prepend():
    lst = SinglyLinkedList()
    lst.prepend(1)
    lst.prepend(2)
    lst.prepend(3)

    assert list(lst) == [3, 2, 1]
    assert len(lst) == 3
    assert lst.head.value == 3
    assert lst.tail.value == 1


def test_insert_middle():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(3)
    lst.insert(1, 2)

    assert list(lst) == [1, 2, 3]
    assert len(lst) == 3


def test_insert_at_begin_and_end():
    lst = SinglyLinkedList()
    lst.insert(0, "a")
    lst.insert(1, "c")
    lst.insert(1, "b")

    assert list(lst) == ["a", "b", "c"]


def test_insert_out_of_range():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.insert(1, "x")


def test_remove_at_middle():
    lst = SinglyLinkedList()
    for i in range(5):
        lst.append(i)

    lst.remove_at(2)
    assert list(lst) == [0, 1, 3, 4]
    assert len(lst) == 4


def test_remove_at_head():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)

    lst.remove_at(0)
    assert list(lst) == [2]
    assert lst.head.value == 2
    assert lst.tail.value == 2


def test_remove_at_tail():
    lst = SinglyLinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)

    lst.remove_at(2)
    assert list(lst) == [1, 2]
    assert lst.tail.value == 2


def test_remove_single_element():
    lst = SinglyLinkedList()
    lst.append(42)

    lst.remove_at(0)
    assert len(lst) == 0
    assert lst.head is None
    assert lst.tail is None


def test_remove_out_of_range():
    lst = SinglyLinkedList()
    with pytest.raises(IndexError):
        lst.remove_at(0)


def test_repr_and_pretty():
    lst = SinglyLinkedList()
    lst.append("A")
    lst.append("B")

    assert repr(lst) == "SinglyLinkedList(['A', 'B'])"
    assert lst.pretty() == "[A] -> [B] -> None"
