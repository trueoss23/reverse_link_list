from list_single_type import ListSingleType
from exceptions import UncorrectValueType, EmptyList
import pytest


def test_create_list_succes():
    x = ListSingleType()
    assert x.size == 0
    assert x.is_empty()


def test_add_3_int_values_to_tail_success():
    x = ListSingleType()
    x.add_to_tail(1)
    x.add_to_tail(-2)
    x.add_to_tail(3)
    assert x.size == 3


def test_add_values_UncorrectValueType():
    x = ListSingleType()
    x.add_to_tail(1)
    with pytest.raises(UncorrectValueType):
        x.add_to_tail('2')


def test_add_values_to_head_succes():
    x = ListSingleType()
    x.add_to_head('14')
    size1 = x.size

    x.add_to_head('pes')
    size2 = x.size
    head = x.head.data

    assert size1 == 1
    assert size2 == 2
    assert head == 'pes'


def test_add_to_head_and_tail():
    x = ListSingleType()
    x.add_to_head('14')
    size1 = x.size

    x.add_to_tail('pes')
    size2 = x.size
    head = x.head.data

    assert size1 == 1
    assert size2 == 2
    assert head == '14'


def test_add_to_head_UncorrectValueType():
    x = ListSingleType()
    x.add_to_head('14')
    with pytest.raises(UncorrectValueType):
        x.add_to_head(1)


def test_remove_elem_any_types_succes():
    x = ListSingleType()
    x.add_to_tail(5)
    size1 = x.size
    res_del1 = x.remove(5)
    size2 = x.size
    state1 = x.is_empty()

    x.add_to_head('5')
    size3 = x.size
    res_del2 = x.remove('5')
    size4 = x.size
    state2 = x.is_empty()
    x.vision_list()

    assert state1
    assert state2
    assert res_del1
    assert res_del2
    assert size1 == 1
    assert size2 == 0
    assert size3 == 1
    assert size4 == 0


def test_remove_elem_in_middle_list_succes():
    x = ListSingleType()
    x.add_to_tail(5)
    x.add_to_tail(6)
    x.add_to_tail(7)
    x.add_to_tail(9)
    res_del = x.remove(7)
    size = x.size

    assert res_del
    assert size == 3


def test_remove_elem_in_tail_list_succes():
    x = ListSingleType()
    x.add_to_tail('5')
    x.add_to_tail('6')
    x.add_to_tail('7')
    x.add_to_tail('9')
    res_del = x.remove('9')
    size = x.size

    assert res_del
    assert size == 3


def test_remove_elem_what_not_be_in_list_success():
    x = ListSingleType()
    x.add_to_tail([1, 2, 3])
    x.add_to_tail([5, 5, 5])
    x.add_to_tail([])
    x.add_to_tail([1, 3, 4])
    x.vision_list()
    res_del = x.remove([1, 5])
    size = x.size

    assert not res_del
    assert size == 4


def test_remove_elem_what_not_be_in_list_EmptyList():
    x = ListSingleType()
    with pytest.raises(EmptyList):
        x.remove(1241241241)


def test_remove_elem_what_not_be_in_list_UncorrectValueTypet():
    x = ListSingleType()
    x.add_to_head('12412412')
    with pytest.raises(UncorrectValueType):
        x.remove(1241241241)
