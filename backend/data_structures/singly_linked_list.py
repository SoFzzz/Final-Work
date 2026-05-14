# backend/data_structures/singly_linked_list.py
# Singly linked list implementation using nodes with a single forward pointer.
#
# Structure: Chain of nodes; each node contains data and a reference to the next node.
# Used for: Dynamic customer registration.
# Behavior: Nodes are allocated on demand; traversal is unidirectional (from head to tail).


class Node:
    """Node for the singly linked list."""
    def __init__(self, data):
        # Stores the node data
        self.data = data
        # Pointer to the next node, initially null
        self.next = None

    def __str__(self):
        return f"Node({self.data})"

    def __repr__(self):
        return f"Node(data={self.data!r})"


class SinglyLinkedList:
    """Implementation of the singly linked list."""
    def __init__(self):
        # Pointer to the head of the list
        self.head = None
        # Internal size counter
        self._size = 0

    def add_to_head(self, data):
        """Inserts a new node at the beginning of the list."""
        if data is None:
            raise ValueError("Cannot add None data to the list")
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_to_tail(self, data):
        """Inserts a new node at the end of the list."""
        if data is None:
            raise ValueError("Cannot add None data to the list")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, data):
        """Finds and removes the first node containing the given data."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if previous is None:
                    # The node to remove is the head
                    self.head = current.next
                else:
                    # The node to remove is in the middle or at the end
                    previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
        
        # The node was not found
        return False

    def search(self, data):
        """Returns the node containing the given data, or None if not found."""
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def traverse(self):
        """Iterates and prints all nodes from head to tail."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")

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
        return f"SinglyLinkedList([{', '.join(elements)}])"

    def __repr__(self):
        return f"SinglyLinkedList(size={self._size}, head={self.head})"


if __name__ == "__main__":
    # Usage example: Customer Registration
    print("=" * 60)
    print("SINGLY LINKED LIST - CUSTOMER REGISTRATION EXAMPLE")
    print("=" * 60)

    registry = SinglyLinkedList()

    customers = [
        "Customer #1 - Alice",
        "Customer #2 - Bob",
        "Customer #3 - Charlie"
    ]

    print("\n1. Adding customers to the tail of the registry:")
    for customer in customers:
        registry.add_to_tail(customer)
        print(f"   [OK] Added to tail: {customer}")

    print("\n2. Adding a customer to the head:")
    head_customer = "Customer #0 - Admin"
    registry.add_to_head(head_customer)
    print(f"   [OK] Added to head: {head_customer}")

    print(f"\n3. Total registered customers: {registry.size()}")
    print("   Current registry traversal:")
    print("   ", end="")
    registry.traverse()

    search_target = "Customer #2 - Bob"
    print(f"\n4. Searching for '{search_target}':")
    found_node = registry.search(search_target)
    if found_node:
        print(f"   Found node: {found_node}")

    print("\n5. Removing a customer:")
    remove_target = "Customer #1 - Alice"
    if registry.remove(remove_target):
        print(f"   [OK] Removed: {remove_target}")

    print("\n6. Final registry state:")
    print("   ", end="")
    registry.traverse()

    print("\n" + "=" * 60)
