# backend/data_structures/circular_doubly_linked_list.py
# Circular doubly linked list implementation.
#
# Structure:   Chain of nodes with both 'next' and 'prev' pointers connected circularly:
#              last.next -> first  and  first.prev -> last.
# Used for:    Weekly promotions navigation.
# Behavior:    Promotions can be browsed forward or backward without ever hitting a boundary.
#              navigate_forward() and navigate_backward() loop endlessly around the list.


class CircularDoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self._size = 0

    def is_empty(self):
        """Return True if the list has no nodes."""
        return self._size == 0

    def size(self):
        """Return the total number of nodes in the list."""
        return self._size

    def add(self, data):
        """Insert a new node and update all four circular pointers:
        new_node.next -> head, head.prev -> new_node,
        previous_tail.next -> new_node, new_node.prev -> previous_tail.
        """
        new_node = CircularDoubleNode(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
            self.current = self.head
        else:
            tail = self.head.prev          # the current last node
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self._size += 1

    def navigate_forward(self):
        """Advance current to current.next and return its data."""
        if self.is_empty():
            return None
        self.current = self.current.next
        return self.current.data

    def navigate_backward(self):
        """Move current to current.prev and return its data."""
        if self.is_empty():
            return None
        self.current = self.current.prev
        return self.current.data

    def display_current(self):
        """Print the data stored in the current node."""
        if self.is_empty():
            print("  (no promotions available)")
        else:
            print(f"  Current promotion: {self.current.data}")

    def display(self):
        """Print all nodes starting from head, stopping after one full loop."""
        if self.is_empty():
            print("  (no promotions registered)")
            return
        node = self.head
        items = []
        for _ in range(self._size):
            items.append(str(node.data))
            node = node.next
        print(" <-> ".join(items) + " <-> [circular]")
