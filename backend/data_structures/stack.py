# backend/data_structures/stack.py
# Stack implementation following LIFO (Last In, First Out) discipline.
#
# Structure: Restricted linear structure; access is strictly limited to the top element.
# Use Case: Tracking canceled sales and returns.
# Behavior: The most recent cancellation is always processed first.
#           Push adds a cancellation; pop retrieves and removes the most recent one.


class Stack:
    """
    Custom stack implementation managing a sequential LIFO collection.

    Use Case: Store canceled sales and returns to process the most
    recent reversal action first.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []
        self.top = -1

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The element to be added to the stack.

        Returns:
            bool: True if the item was added successfully.
        """
        if item is None:
            raise ValueError("Cannot push None onto the stack")

        self.items.append(item)
        self.top += 1
        return True

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Returns:
            The most recently pushed element.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        item = self.items.pop()
        self.top -= 1
        return item

    def peek(self):
        """
        Returns the top element without removing it.

        Returns:
            The element currently at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")

        return self.items[self.top]

    def is_empty(self):
        """
        Checks if the stack contains any elements.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top == -1

    def size(self):
        """
        Gets the total number of elements currently in the stack.

        Returns:
            int: Current size of the stack.
        """
        return self.top + 1

    def display(self):
        """
        Prints the contents of the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
            return

        for index in range(self.top, -1, -1):
            print(f"[{index}] {self.items[index]}")

    def __str__(self):
        return f"Stack(top={self.top}, items={self.items})"

    def __repr__(self):
        return f"Stack(size={self.size()}, items={self.items})"


if __name__ == "__main__":
    # Usage example: Canceled Sales Tracking
    print("=" * 60)
    print("STACK - CANCELED SALES EXAMPLE")
    print("=" * 60)

    stack = Stack()

    cancellations = [
        "Sale #101 - The Great Gatsby",
        "Sale #102 - 1984",
        "Sale #103 - Pride and Prejudice",
    ]

    print("\n1. Pushing canceled sales onto the stack:")
    for cancellation in cancellations:
        stack.push(cancellation)
        print(f"   [OK] Pushed: {cancellation}")

    print(f"\n2. Current top item: {stack.peek()}")
    print(f"3. Current stack size: {stack.size()}")

    print("\n4. Stack contents (top to bottom):")
    stack.display()

    popped = stack.pop()
    print(f"\n5. Popped latest cancellation: {popped}")
    print(f"6. New top item: {stack.peek()}")

    print("\n7. Final stack state:")
    stack.display()

    print("\n" + "=" * 60)
