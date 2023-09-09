from list_single_type import ListSingleType


# def reverse_list(my_list: ListSingleType) -> ListSingleType:
#     if my_list.is_empty():
#         return my_list
#     result = ListSingleType()
#     current = my_list.head
#     while current.next:
#         result.add_to_head(current.data)
#         current = current.next
#     result.add_to_head(current.data)
#     return result

def reverse_list(my_list: ListSingleType) -> ListSingleType:
    current = my_list.head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    my_list.head = prev
    return my_list
