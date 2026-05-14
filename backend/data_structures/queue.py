# backend/data_structures/queue.py
# Queue implementation following FIFO (First In, First Out) discipline.
#
# Estructura:  Estructura lineal restringida; los elementos entran por atras y salen por delante.
# Uso:         Gestion de la fila de espera de clientes.
# Comportamiento: Los clientes son atendidos exactamente en el orden en que llegan.
#                Enqueue agrega un cliente al final; dequeue atiende al cliente del frente.


class Queue:
    """
    Implementacion personalizada de una cola usando una lista de Python.

    Caso de uso: almacenar clientes en espera para atenderlos en orden FIFO.
    """

    def __init__(self):
        """Inicializa una cola vacia."""
        self.items = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        """
        Agrega un elemento al final de la cola.

        Args:
            item: Elemento que se desea agregar.

        Returns:
            bool: True si el elemento se agrega correctamente.
        """
        if item is None:
            raise ValueError("Cannot enqueue None into the queue")

        self.items.append(item)
        self.rear += 1
        return True

    def dequeue(self):
        """
        Elimina y retorna el elemento que esta al frente de la cola.

        Returns:
            El elemento que ha esperado por mas tiempo.
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")

        item = self.items.pop(0)
        self.rear -= 1
        if self.is_empty():
            self.front = 0
            self.rear = -1
        return item

    def peek(self):
        """
        Retorna el elemento del frente sin eliminarlo.

        Returns:
            El siguiente elemento que saldra de la cola.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty queue")

        return self.items[self.front]

    def is_empty(self):
        """
        Verifica si la cola contiene elementos.

        Returns:
            bool: True si la cola esta vacia.
        """
        return len(self.items) == 0

    def size(self):
        """
        Obtiene la cantidad de elementos almacenados en la cola.

        Returns:
            int: Tamano actual de la cola.
        """
        return len(self.items)

    def display(self):
        """
        Imprime todos los elementos de la cola desde el frente hasta el final.
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
