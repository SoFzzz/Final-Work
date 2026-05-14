# backend/data_structures/queue.py
# Queue implementation following FIFO (First In, First Out) discipline.
#
# Structure: Restricted linear structure; elements enter from the rear and leave from the front.
# Use Case: Managing the customer waiting line.
# Behavior: Customers are attended in the exact order of their arrival.
#           Enqueue adds a customer to the rear; dequeue attends to the customer at the front.


class Queue:
    """
    Custom queue implementation managing a sequential FIFO collection.

    Use Case: Store waiting customers to attend to them in FIFO order.
    """

    def __init__(self):
        """Initializes an empty queue."""
        self.items = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        """
        Adds an element to the rear of the queue.

        Args:
            item: The element to be added to the queue.

        Returns:
            bool: True if the element was added successfully.
        """
        if item is None:
            raise ValueError("Cannot enqueue None into the queue")

        self.items.append(item)
        self.rear += 1
        return True

    def dequeue(self):
        """
        Removes and returns the element at the front of the queue.
        Returns None if the queue is empty instead of raising an exception,
        preventing crashes when the customer waiting line is empty.

        Returns:
            The element that has been waiting the longest, or None if empty.
        """
        if self.is_empty():
            return None

        item = self.items.pop(0)
        self.rear -= 1
        if self.is_empty():
            self.front = 0
            self.rear = -1
        return item

    def peek(self):
        """
        Returns the front element without removing it.
        Returns None if the queue is empty.

        Returns:
            The next element to be dequeued, or None if empty.
        """
        if self.is_empty():
            return None

        return self.items[self.front]

    def is_empty(self):
        """
        Checks if the queue contains any elements.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Gets the total number of elements currently in the queue.

        Returns:
            int: Current size of the queue.
        """
        return len(self.items)

    def display(self):
        """
        Prints all elements in the queue from front to rear.
        """
        if self.is_empty():
            print("Queue is empty.")
            return

        for index, item in enumerate(self.items):
            print(f"[{index}] {item}")

    def __str__(self):
        return f"Queue(front={self.front}, rear={self.rear}, items={self.items})"

    def __repr__(self):
        return f"Queue(size={self.size()}, items={self.items})"


if __name__ == "__main__":
    # Usage example: Customer Waiting Line
    print("=" * 60)
    print("QUEUE - CUSTOMER WAITING LINE EXAMPLE")
    print("=" * 60)

    queue = Queue()

    customers = [
        "Customer #1 - Ana",
        "Customer #2 - Luis",
        "Customer #3 - Sofia",
    ]

    print("\n1. Enqueuing arriving customers:")
    for customer in customers:
        queue.enqueue(customer)
        print(f"   [OK] Enqueued: {customer}")

    print(f"\n2. Next customer to attend: {queue.peek()}")
    print(f"3. Current queue size: {queue.size()}")

    print("\n4. Queue contents (front to rear):")
    queue.display()

    attended = queue.dequeue()
    print(f"\n5. Dequeued attended customer: {attended}")
    print(f"6. New next customer: {queue.peek()}")

    print("\n7. Final queue state:")
    queue.display()

    print("\n" + "=" * 60)
