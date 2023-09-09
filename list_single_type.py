from typing import Any, TypeVar

from exceptions import UncorrectValueType, EmptyList

T = TypeVar('T')


class Node():
    def __init__(self, data: T):
        self.data: T = data
        self.next: T = None


class ListSingleType:
    def __init__(self):
        self.size = 0
        self.type = None
        self.head = None

    def is_empty(self):
        return self.head is None

    def vision_list(self):
        if self.head is None:
            print("List is Empty")
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def add_to_tail(self, value: Any) -> None:
        if self.is_empty():
            new_node = Node(value)
            self.type = type(value)
            self.head = new_node
        else:
            if type(value) != self.type:
                raise UncorrectValueType(f'type of {value} is {type(value)}\
                                         , but type of list is {self.type}')
            new_node = Node(value)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def add_to_head(self, value: Any) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.type = type(value)
            self.head = new_node
        else:
            if type(value) != self.type:
                raise UncorrectValueType(f'type of {value} is {type(value)}\
                                         , but type of list is {self.type}')
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def remove(self, value: Any) -> bool:
        if self.is_empty():
            raise EmptyList('Trying to remove element from an emty list')
        if self.type != type(value):
            raise UncorrectValueType(f'type of {value} is {type(value)}\
                                        , but type of list is {self.type}')
        if self.head.data == value:
            if self.head.next is None:
                self.head = None
                self.size -= 1
                self.type = None
                return True

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

