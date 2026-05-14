# backend/data_structures/circular_singly_linked_list.py
# Circular singly linked list implementation.
#
# Structure:   Chain of nodes where the last node's 'next' pointer connects back to the first,
#              forming a closed loop with no natural end.
# Used for:    Seller rotation system.
# Behavior:    Sellers are cycled continuously and evenly. Calling get_next() always advances
#              to the next seller, wrapping back to the first after the last one is reached.


class CircularNode:
    # TODO: Implement __init__(data) — store data and set next pointer to None
    pass


class CircularSinglyLinkedList:
    # TODO: Implement __init__ — initialize head pointer, current pointer, and size counter

    # TODO: Implement add(data) — insert a new node and maintain the circular link
    #       (new tail's next must always point back to head)

    # TODO: Implement get_next() — advance current to the next node and return its data;
    #       wraps automatically from last node back to head

    # TODO: Implement remove(data) — find and remove a node while preserving the circular link

    # TODO: Implement display() — print all nodes starting from head, stopping after one full loop

    # TODO: Implement is_empty() — return True if the list has no nodes

    # TODO: Implement size() — return the total number of nodes in the list

    pass
