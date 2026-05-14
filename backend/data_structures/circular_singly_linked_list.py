# backend/data_structures/circular_singly_linked_list.py
# Circular singly linked list implementation.
#
# Structure:   Chain of nodes where the last node's 'next' pointer connects back to the first,
#              forming a closed loop with no natural end.
# Used for:    Seller rotation system.
# Behavior:    Sellers are cycled continuously and evenly. Calling get_next() always advances
#              to the next seller, wrapping back to the first after the last one is reached.


class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
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
        """Insert a new node and maintain the circular link.
        The new tail's next must always point back to head.
        """
        new_node = CircularNode(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head          # points to itself
            self.current = self.head
        else:
            # Walk to the current tail
            tail = self.head
            while tail.next is not self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head          # restore circular link
        self._size += 1

    def get_next(self):
        """Advance current to the next node and return its data.
        Wraps automatically from the last node back to head.
        """
        if self.is_empty():
            return None
        data = self.current.data
        self.current = self.current.next
        return data

    def remove(self, data):
        """Find and remove a node while preserving the circular link."""
        if self.is_empty():
            return False

        # Single-element case
        if self._size == 1:
            if self.head.data == data:
                self.head = None
                self.current = None
                self._size -= 1
                return True
            return False

        # Walk to find the node and its predecessor
        prev = self.head
        while prev.next is not self.head:
            prev = prev.next
        # prev is now the tail; restart from head
        tail = prev

        node = self.head
        prev = tail

        for _ in range(self._size):
            if node.data == data:
                if node is self.head:
                    # Move head forward and relink tail
                    self.head = self.head.next
                    tail.next = self.head
                    if self.current is node:
                        self.current = self.head
                else:
                    prev.next = node.next
                    if self.current is node:
                        self.current = node.next
                self._size -= 1
                return True
            prev = node
            node = node.next

        return False

    def display(self):
        """Print all nodes starting from head, stopping after one full loop."""
        if self.is_empty():
            print("  (empty seller rotation)")
            return
        node = self.head
        items = []
        for _ in range(self._size):
            items.append(str(node.data))
            node = node.next
        print(" -> ".join(items) + " -> [back to start]")
