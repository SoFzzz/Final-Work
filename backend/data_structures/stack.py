# backend/data_structures/stack.py
# Stack implementation following LIFO (Last In, First Out) discipline.
#
# Estructura:  Estructura lineal restringida; el acceso se limita solo al elemento superior.
# Uso:         Seguimiento de ventas canceladas y devoluciones.
# Comportamiento: La cancelacion mas reciente se procesa primero.
#                Push agrega una cancelacion; pop recupera y elimina la mas reciente.


class Stack:
    """
    Implementacion personalizada de una pila usando una lista de Python.

    Caso de uso: almacenar ventas canceladas y devoluciones para
    procesar primero la accion mas reciente.
    """

    def __init__(self):
        """Inicializa una pila vacia."""
        self.items = []
        self.top = -1

    def push(self, item):
        """
        Agrega un elemento en la parte superior de la pila.

        Args:
            item: Elemento que se desea agregar.

        Returns:
            bool: True si el elemento se almacena correctamente.
        """
        if item is None:
            raise ValueError("Cannot push None onto the stack")

        self.items.append(item)
        self.top += 1
        return True

    def pop(self):
        """
        Elimina y retorna el elemento que esta en la cima de la pila.

        Returns:
            El elemento agregado mas recientemente.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")

        item = self.items.pop()
        self.top -= 1
        return item

    def peek(self):
        """
        Retorna el elemento superior sin eliminarlo.

        Returns:
            El elemento que se encuentra actualmente en la cima.
        """
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack")

        return self.items[self.top]

    def is_empty(self):
        """
        Verifica si la pila contiene elementos.

        Returns:
            bool: True si la pila esta vacia.
        """
        return self.top == -1

    def size(self):
        """
        Obtiene la cantidad de elementos almacenados en la pila.

        Returns:
            int: Tamano actual de la pila.
        """
        return self.top + 1

    def display(self):
        """
        Imprime el contenido de la pila desde la cima hasta la base.
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
