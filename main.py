from list_single_type import ListSingleType
from operation_for_list import reverse_list


if __name__ == "__main__":
    x = ListSingleType()
    x.add_to_tail(1)
    x.add_to_tail(2)
    x.add_to_tail(3)
    x.vision_list()
    x = reverse_list(x)
    print()
    x.vision_list()
