# backend/data_structures/doubly_linked_list.py
# Doubly linked list implementation using nodes with forward and backward pointers.
#
# Structure: Chain of nodes; each node contains data, a reference to the next, and one to the previous.
# Used for: Tracking sales history.
# Behavior: Supports bidirectional traversal — forward (oldest to most recent)
#           and backward (most recent to oldest) through the complete sales history.


class DoubleNode:
    """Node for the doubly linked list."""
    def __init__(self, data):
        # Stores the node data
        self.data = data
        # Pointer to the next node
        self.next = None
        # Pointer to the previous node
        self.prev = None

    def __str__(self):
        return f"DoubleNode({self.data})"

    def __repr__(self):
        return f"DoubleNode(data={self.data!r})"


class DoublyLinkedList:
    """Implementation of the doubly linked list."""
    def __init__(self):
        # Pointer to the head of the list
        self.head = None
        # Pointer to the tail of the list
        self.tail = None
        # Internal size counter
        self._size = 0

    def add_to_tail(self, data):
        """Inserts a new node at the end (most recent sale)."""
        if data is None:
            raise ValueError("Cannot add None data to the list")
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def add_to_head(self, data):
        """Inserts a new node at the beginning."""
        if data is None:
            raise ValueError("Cannot add None data to the list")
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def remove(self, data):
        """Finds and removes the node containing the given data, updating neighbor pointers correctly."""
        current = self.head

        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    # The node is not the head
                    current.prev.next = current.next
                else:
                    # The node is the head
                    self.head = current.next

                if current.next is not None:
                    # The node is not the tail
                    current.next.prev = current.prev
                else:
                    # The node is the tail
                    self.tail = current.prev

                self._size -= 1
                return True
            
            current = current.next

        # The node was not found
        return False

    def traverse_forward(self):
        """Iterates and prints all nodes from head to tail."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")

    def traverse_backward(self):
        """Iterates and prints all nodes from tail to head.
        Correctly handles lists with a single element (tail.prev is None).
        """
        if self.is_empty():
            print("Empty list")
            return
        current = self.tail
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.prev
        print(" -> ".join(elements))

    def is_empty(self):
        """Returns True if the list has no nodes."""
        return self.head is None

    def size(self):
        """Returns the total number of nodes in the list."""
        return self._size

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(repr(current.data))
            current = current.next
        return f"DoublyLinkedList([{', '.join(elements)}])"

    def __repr__(self):
        return f"DoublyLinkedList(size={self._size}, head={self.head}, tail={self.tail})"


if __name__ == "__main__":
    # Usage example: Sales History Tracking
    print("=" * 60)
    print("DOUBLY LINKED LIST - SALES HISTORY EXAMPLE")
    print("=" * 60)

    history = DoublyLinkedList()

    sales = [
        "Sale #1 - Book: 1984",
        "Sale #2 - Book: The Great Gatsby",
        "Sale #3 - Book: To Kill a Mockingbird"
    ]

    print("\n1. Adding completed sales to history (tail):")
    for sale in sales:
        history.add_to_tail(sale)
        print(f"   [OK] Recorded: {sale}")

    print(f"\n2. Total records in history: {history.size()}")
    
    print("\n3. Forward Traversal (Chronological: Oldest to Newest):")
    print("   ", end="")
    history.traverse_forward()

    print("\n4. Backward Traversal (Reverse Chronological: Newest to Oldest):")
    print("   ", end="")
    history.traverse_backward()

    print("\n5. Removing a sale record from history:")
    remove_target = "Sale #2 - Book: The Great Gatsby"
    if history.remove(remove_target):
        print(f"   [OK] Removed: {remove_target}")

    print("\n6. History state after removal (Forward Traversal):")
    print("   ", end="")
    history.traverse_forward()

    print("\n" + "=" * 60)
