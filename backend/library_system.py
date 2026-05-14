# backend/library_system.py
# Core business logic and integration layer for the Library Management System.
# Coordinates all interactions between domain models and data structures.


class LibrarySystem:
    # TODO: Import and instantiate all data structures in __init__:
    #
    #       self.book_catalog       = SimpleList()               — book storage
    #       self.price_lists        = DoubleList()               — normal and discounted prices
    #       self.customer_registry  = SinglyLinkedList()         — dynamic customer records
    #       self.sales_history      = DoublyLinkedList()         — full sales record (bidirectional)
    #       self.cancellation_stack = Stack()                    — canceled sales / returns
    #       self.customer_queue     = Queue()                    — customers waiting for service
    #       self.seller_rotation    = CircularSinglyLinkedList() — seller assignment cycle
    #       self.promotions         = CircularDoublyLinkedList() — weekly promotion browser

    # --- Book Management ---
    # TODO: Implement register_book(book) — add a Book to the catalog
    # TODO: Implement list_books() — display all books in the catalog
    # TODO: Implement search_book(query) — search by title or author

    # --- Customer Management ---
    # TODO: Implement register_customer(customer) — add a Customer to the registry
    # TODO: Implement add_customer_to_queue(customer) — place a customer in the waiting queue
    # TODO: Implement attend_next_customer() — dequeue front customer and assign a seller

    # --- Seller Management ---
    # TODO: Implement register_seller(seller) — add a Seller to the rotation
    # TODO: Implement assign_next_seller() — return the next seller in the circular rotation

    # --- Sales Management ---
    # TODO: Implement process_sale(customer, book, seller) — record a completed sale
    # TODO: Implement cancel_sale(sale) — push a canceled sale onto the cancellation stack
    # TODO: Implement process_return() — pop the most recent cancellation from the stack

    # --- History and Reporting ---
    # TODO: Implement view_sales_history() — traverse and display the full sales history
    # TODO: Implement view_canceled_sales() — display all entries in the cancellation stack

    # --- Promotions Management ---
    # TODO: Implement add_promotion(promotion) — add a weekly promotion to the circular list
    # TODO: Implement next_promotion() — navigate forward to the next promotion
    # TODO: Implement previous_promotion() — navigate backward to the previous promotion

    pass
