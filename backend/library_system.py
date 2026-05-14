# backend/library_system.py
# Core business logic and integration layer for the Library Management System.
# Coordinates all interactions between domain models and data structures.

from backend.data_structures.simple_list import SimpleList
from backend.data_structures.double_list import DoubleList
from backend.data_structures.singly_linked_list import SinglyLinkedList
from backend.data_structures.doubly_linked_list import DoublyLinkedList
from backend.data_structures.stack import Stack
from backend.data_structures.queue import Queue
from backend.data_structures.circular_singly_linked_list import CircularSinglyLinkedList
from backend.data_structures.circular_doubly_linked_list import CircularDoublyLinkedList
from backend.models import Book, Customer, Seller, Sale, Promotion
import datetime


class LibrarySystem:
    """Central coordinator for all bookstore operations.
    Connects domain models with their corresponding data structures.
    """

    def __init__(self):
        self.book_catalog       = SimpleList()               # book storage
        self.price_lists        = DoubleList()               # normal and discounted prices
        self.customer_registry  = SinglyLinkedList()         # dynamic customer records
        self.sales_history      = DoublyLinkedList()         # full sales record (bidirectional)
        self.cancellation_stack = Stack()                    # canceled sales / returns
        self.customer_queue     = Queue()                    # customers waiting for service
        self.seller_rotation    = CircularSinglyLinkedList() # seller assignment cycle
        self.promotions         = CircularDoublyLinkedList() # weekly promotion browser

        self._sale_counter = 0   # auto-increment sale IDs

    # -----------------------------------------------------------------------
    # Book Management
    # -----------------------------------------------------------------------

    def register_book(self, book: Book):
        """Add a Book to the catalog and register its price pair."""
        self.book_catalog.add(book)
        self.price_lists.add_pair(book.price, round(book.price * 0.85, 2))
        print(f"  [OK] Book registered: {book}")

    def list_books(self):
        """Display all books currently in the catalog."""
        if self.book_catalog.is_empty():
            print("  No books in catalog.")
            return
        print("  --- Book Catalog ---")
        self.book_catalog.display()

    def search_book(self, query: str):
        """Search books by title or author (case-insensitive)."""
        query_lower = query.lower()
        results = []
        for i in range(self.book_catalog.size()):
            book = self.book_catalog.get(i)
            if book and (query_lower in book.title.lower() or query_lower in book.author.lower()):
                results.append(book)
        if not results:
            print(f"  No books found matching '{query}'.")
        else:
            print(f"  --- Search results for '{query}' ---")
            for book in results:
                print(f"    {book}")

    # -----------------------------------------------------------------------
    # Customer Management
    # -----------------------------------------------------------------------

    def register_customer(self, customer: Customer):
        """Add a Customer to the registry (singly linked list)."""
        self.customer_registry.add_to_tail(customer)
        print(f"  [OK] Customer registered: {customer}")

    def add_customer_to_queue(self, customer: Customer):
        """Place a customer in the waiting queue (FIFO)."""
        self.customer_queue.enqueue(customer)
        print(f"  [OK] Customer added to queue: {customer.name}")

    def attend_next_customer(self):
        """Dequeue the front customer and assign the next available seller.
        Returns a tuple (customer, seller) or None if queue is empty.
        """
        if self.customer_queue.is_empty():
            print("  No customers in the waiting queue.")
            return None
        if self.seller_rotation.is_empty():
            print("  No sellers registered in the rotation system.")
            return None
        customer = self.customer_queue.dequeue()
        seller   = self.seller_rotation.get_next()
        print(f"  [OK] Attending: {customer.name}  —  Assigned seller: {seller.name}")
        return customer, seller

    # -----------------------------------------------------------------------
    # Seller Management
    # -----------------------------------------------------------------------

    def register_seller(self, seller: Seller):
        """Add a Seller to the circular rotation."""
        self.seller_rotation.add(seller)
        print(f"  [OK] Seller registered: {seller}")

    def assign_next_seller(self):
        """Return the next seller in the circular rotation without dequeuing anyone."""
        if self.seller_rotation.is_empty():
            print("  No sellers in rotation.")
            return None
        seller = self.seller_rotation.get_next()
        print(f"  [OK] Next seller: {seller.name}")
        return seller

    # -----------------------------------------------------------------------
    # Sales Management
    # -----------------------------------------------------------------------

    def process_sale(self, customer: Customer, book: Book, seller: Seller, quantity: int = 1):
        """Record a completed sale into the sales history (doubly linked list)."""
        if book.stock < quantity:
            print(f"  [ERROR] Insufficient stock for '{book.title}'. Available: {book.stock}")
            return None
        self._sale_counter += 1
        total_price = book.price * quantity
        date = datetime.date.today().isoformat()
        sale = Sale(self._sale_counter, customer, seller, book, quantity, total_price, date)
        book.stock -= quantity
        seller.sales_count += 1
        self.sales_history.add_to_tail(sale)
        print(f"  [OK] Sale processed: {sale}")
        return sale

    def cancel_sale(self, sale: Sale):
        """Push a canceled sale onto the cancellation stack."""
        sale.status = "Cancelled"
        self.cancellation_stack.push(sale)
        print(f"  [OK] Sale #{sale.sale_id} cancelled and pushed to stack.")

    def process_return(self):
        """Pop the most recent cancellation from the stack and restore stock."""
        if self.cancellation_stack.is_empty():
            print("  No cancelled sales to process.")
            return None
        sale = self.cancellation_stack.pop()
        sale.book.stock += sale.quantity
        sale.seller.sales_count -= 1
        sale.status = "Returned"
        print(f"  [OK] Return processed for Sale #{sale.sale_id} — stock restored.")
        return sale

    # -----------------------------------------------------------------------
    # History and Reporting
    # -----------------------------------------------------------------------

    def get_last_sale(self):
        """Return the most recent sale from the doubly linked list tail, or None."""
        if self.sales_history.is_empty():
            return None
        return self.sales_history.tail.data

    def view_sales_history(self):
        """Traverse and display the full sales history (forward)."""
        if self.sales_history.is_empty():
            print("  No sales recorded yet.")
            return
        print("  --- Sales History ---")
        self.sales_history.traverse_forward()

    def view_canceled_sales(self):
        """Display all entries in the cancellation stack without removing them."""
        if self.cancellation_stack.is_empty():
            print("  No cancelled sales on record.")
            return
        print("  --- Cancelled Sales Stack ---")
        self.cancellation_stack.display()

    # -----------------------------------------------------------------------
    # Promotions Management
    # -----------------------------------------------------------------------

    def add_promotion(self, promotion: Promotion):
        """Add a weekly promotion to the circular doubly linked list."""
        self.promotions.add(promotion)
        print(f"  [OK] Promotion added: {promotion}")

    def next_promotion(self):
        """Navigate forward to the next promotion and display it."""
        if self.promotions.is_empty():
            print("  No promotions available.")
            return None
        promo = self.promotions.navigate_forward()
        print(f"  [>>] Next promotion: {promo}")
        return promo

    def previous_promotion(self):
        """Navigate backward to the previous promotion and display it."""
        if self.promotions.is_empty():
            print("  No promotions available.")
            return None
        promo = self.promotions.navigate_backward()
        print(f"  [<<] Previous promotion: {promo}")
        return promo

    def view_current_promotion(self):
        """Display the currently selected promotion."""
        self.promotions.display_current()
