from list_single_type import ListSingleType
from operation_for_list import reverse_list


def test_reverse_list_add_to_head_success():
    x = ListSingleType()
    x.add_to_head(3)
    x.add_to_head(2)
    x.add_to_head(1)
    x.vision_list()
    x = reverse_list(x)
    head = x.head.data

    assert head == 3
    assert x.size == 3
    x.vision_list()


def test_reverse_list_add_to_tail_success():
    x = ListSingleType()
    x.add_to_tail(3)
    x.add_to_tail(2)
    x.add_to_tail(1)
    x.vision_list()
    x = reverse_list(x)
    head = x.head.data

    assert head == 1
    assert x.size == 3
    x.vision_list()


def test_reverse_empty_list_success():
    x = ListSingleType()
    x = reverse_list(x)

    assert x.size == 0
    x.vision_list()


def test_reverse_one_size_list_success():
    x = ListSingleType()
    x.add_to_head('12412412')
    x = reverse_list(x)

    assert x.size == 1
    x.vision_list()
