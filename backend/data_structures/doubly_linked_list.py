# backend/data_structures/doubly_linked_list.py
# Implementación de lista doblemente enlazada usando nodos con punteros hacia adelante y hacia atrás.
#
# Estructura: Cadena de nodos; cada nodo contiene datos, una referencia al siguiente y una al anterior.
# Usado para: Seguimiento del historial de ventas.
# Comportamiento: Soporta recorrido bidireccional — hacia adelante (más antiguo al más reciente) 
#                 y hacia atrás (más reciente al más antiguo) a través del historial completo de ventas.

class DoubleNode:
    """Nodo para la lista doblemente enlazada."""
    def __init__(self, data):
        # Almacena los datos del nodo
        self.data = data
        # Puntero al siguiente nodo
        self.next = None
        # Puntero al nodo anterior
        self.prev = None

class DoublyLinkedList:
    """Implementación de la lista doblemente enlazada."""
    def __init__(self):
        # Puntero a la cabeza de la lista
        self.head = None
        # Puntero a la cola de la lista
        self.tail = None
        # Contador del tamaño de la lista
        self._size = 0

    def add_to_tail(self, data):
        """Inserta un nuevo nodo al final (venta más reciente)."""
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
        """Inserta un nuevo nodo al inicio."""
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
        """Encuentra y elimina el nodo que contiene los datos dados, actualizando los punteros vecinos correctamente."""
        current = self.head

        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    # El nodo no es la cabeza
                    current.prev.next = current.next
                else:
                    # El nodo es la cabeza
                    self.head = current.next

                if current.next is not None:
                    # El nodo no es la cola
                    current.next.prev = current.prev
                else:
                    # El nodo es la cola
                    self.tail = current.prev

                self._size -= 1
                return True
            
            current = current.next

        # El nodo no se encontró
        return False

    def traverse_forward(self):
        """Itera e imprime todos los nodos desde la cabeza hasta la cola."""
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista vacía")

    def traverse_backward(self):
        """Itera e imprime todos los nodos desde la cola hasta la cabeza."""
        current = self.tail
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.prev
        print(" -> ".join(elements) if elements else "Lista vacía")

    def is_empty(self):
        """Retorna True si la lista no tiene nodos."""
        return self.head is None

    def size(self):
        """Retorna el número de nodos en la lista."""
        return self._size
