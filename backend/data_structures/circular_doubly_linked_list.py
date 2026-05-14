# backend/data_structures/circular_doubly_linked_list.py
# Circular doubly linked list implementation.
#
# Structure:   Chain of nodes with both 'next' and 'prev' pointers connected circularly:
#              last.next -> first  and  first.prev -> last.
# Used for:    Weekly promotions navigation.
# Behavior:    Promotions can be browsed forward or backward without ever hitting a boundary.
#              navigate_forward() and navigate_backward() loop endlessly around the list.


class CircularDoubleNode:
    # TODO: Implement __init__(data) — store data, set next to None, set prev to None
    pass


class CircularDoublyLinkedList:
    # TODO: Implement __init__ — initialize head pointer, current pointer, and size counter

    # TODO: Implement add(data) — insert a new node and update all four circular pointers:
    #       new_node.next -> head, head.prev -> new_node,
    #       previous_tail.next -> new_node, new_node.prev -> previous_tail

    # TODO: Implement navigate_forward() — advance current to current.next and return its data

    # TODO: Implement navigate_backward() — move current to current.prev and return its data

    # TODO: Implement display_current() — print the data stored in the current node

    # TODO: Implement display() — print all nodes starting from head, stopping after one full loop

    # TODO: Implement is_empty() — return True if the list has no nodes

    # TODO: Implement size() — return the total number of nodes in the list

    pass
