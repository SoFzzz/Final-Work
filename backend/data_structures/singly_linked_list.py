# backend/data_structures/singly_linked_list.py
# Implementación de lista enlazada simple usando nodos con un solo puntero hacia adelante.
#
# Estructura: Cadena de nodos; cada nodo contiene datos y una referencia al siguiente nodo.
# Usado para: Registro dinámico de clientes.
# Comportamiento: Los nodos se asignan bajo demanda; el recorrido es unidireccional (de cabeza a cola).

class Node:
    """Nodo para la lista enlazada simple."""
    def __init__(self, data):
        # Almacena los datos del nodo
        self.data = data
        # Puntero al siguiente nodo, inicialmente nulo
        self.next = None

class SinglyLinkedList:
    """Implementación de la lista enlazada simple."""
    def __init__(self):
        # Puntero a la cabeza de la lista
        self.head = None
        # Contador del tamaño de la lista
        self._size = 0

    def add_to_head(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_to_tail(self, data):
        """Inserta un nuevo nodo al final de la lista."""
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
        """Encuentra y elimina el nodo que contiene los datos dados."""
        current = self.head
        previous = None

        while current is not None:
            if current.data == data:
                if previous is None:
                    # El nodo a eliminar es la cabeza
                    self.head = current.next
                else:
                    # El nodo a eliminar está en el medio o al final
                    previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next
        
        # El nodo no se encontró
        return False

    def search(self, data):
        """Retorna el nodo que contiene los datos dados, o None si no existe."""
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def traverse(self):
        """Itera e imprime todos los nodos desde la cabeza hasta la cola."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista vacía")

    def is_empty(self):
        """Retorna True si la lista no tiene nodos."""
        return self.head is None

    def size(self):
        """Retorna el número de nodos en la lista."""
        return self._size
