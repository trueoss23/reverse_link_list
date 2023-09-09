from list_single_type import ListSingleType


def reverse_list(my_list: ListSingleType) -> ListSingleType:
    if my_list.is_empty():
        return my_list
    result = ListSingleType()
    current = my_list.head
    while current.next:
        result.add_to_head(current.data)
        current = current.next
    result.add_to_head(current.data)
    return result
