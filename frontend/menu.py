# frontend/menu.py
# Console menu interface for the Library Management System.
# Responsible for all user input, output, and navigation between system features.

from backend.library_system import LibrarySystem
from backend.models import Book, Customer, Seller, Sale, Promotion


class Menu:
    """User-facing console interface. Receives a LibrarySystem dependency via injection."""

    def __init__(self, system: LibrarySystem):
        self.system = system

    # -----------------------------------------------------------------------
    # Public entry point
    # -----------------------------------------------------------------------

    def run(self):
        """Start the main application loop."""
        while True:
            self._print_header("MAIN MENU")
            self.display_main_menu()
            choice = self._get_input("Select an option: ")
            if choice == "1":
                self.book_menu()
            elif choice == "2":
                self.customer_menu()
            elif choice == "3":
                self.seller_menu()
            elif choice == "4":
                self.sales_menu()
            elif choice == "5":
                self.returns_menu()
            elif choice == "6":
                self.promotions_menu()
            elif choice == "0":
                print("\n  Goodbye! Thank you for using the Library Management System.\n")
                break
            else:
                print("  [!] Invalid option. Please try again.")

    def display_main_menu(self):
        """Show the top-level option list."""
        print("  1. Book Management")
        print("  2. Customer Management")
        print("  3. Seller Management")
        print("  4. Sales Management")
        print("  5. Returns & Cancellations")
        print("  6. Weekly Promotions")
        print("  0. Exit")
        self._print_separator()

    # -----------------------------------------------------------------------
    # Sub-menus
    # -----------------------------------------------------------------------

    def book_menu(self):
        """Sub-menu for book operations."""
        while True:
            self._print_header("BOOK MANAGEMENT")
            print("  1. Register new book")
            print("  2. List all books")
            print("  3. Search book")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Register Book")
                try:
                    book_id = int(self._get_input("  Book ID       : "))
                    title   = self._get_input("  Title         : ")
                    author  = self._get_input("  Author        : ")
                    genre   = self._get_input("  Genre         : ")
                    year    = int(self._get_input("  Year          : "))
                    price   = float(self._get_input("  Price ($)     : "))
                    stock   = int(self._get_input("  Stock         : "))
                    book = Book(book_id, title, author, genre, year, price, stock)
                    self.system.register_book(book)
                except ValueError:
                    print("  [!] Invalid input. Please enter the correct data types.")

            elif choice == "2":
                self._print_header("Book Catalog")
                self.system.list_books()

            elif choice == "3":
                self._print_header("Search Book")
                query = self._get_input("  Enter title or author: ")
                self.system.search_book(query)

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    def customer_menu(self):
        """Sub-menu for customer operations."""
        while True:
            self._print_header("CUSTOMER MANAGEMENT")
            print("  1. Register new customer")
            print("  2. Add customer to waiting queue")
            print("  3. Attend next customer in queue")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Register Customer")
                try:
                    cust_id = int(self._get_input("  Customer ID   : "))
                    name    = self._get_input("  Name          : ")
                    phone   = self._get_input("  Phone         : ")
                    email   = self._get_input("  Email         : ")
                    customer = Customer(cust_id, name, phone, email)
                    self.system.register_customer(customer)
                except ValueError:
                    print("  [!] Invalid input.")

            elif choice == "2":
                self._print_header("Add Customer to Queue")
                try:
                    cust_id = int(self._get_input("  Customer ID to enqueue: "))
                    node = self.system.customer_registry.search(cust_id)
                    if node:
                        # search() returns a Node; compare by customer_id
                        found = None
                        current = self.system.customer_registry.head
                        while current:
                            if current.data.customer_id == cust_id:
                                found = current.data
                                break
                            current = current.next
                        if found:
                            self.system.add_customer_to_queue(found)
                        else:
                            print(f"  [!] Customer ID {cust_id} not found in registry.")
                    else:
                        print(f"  [!] Customer ID {cust_id} not found in registry.")
                except ValueError:
                    print("  [!] Please enter a valid numeric ID.")

            elif choice == "3":
                self._print_header("Attend Next Customer")
                self.system.attend_next_customer()

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    def seller_menu(self):
        """Sub-menu for seller operations."""
        while True:
            self._print_header("SELLER MANAGEMENT")
            print("  1. Register new seller")
            print("  2. View seller rotation")
            print("  3. Assign next seller (manual rotation)")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Register Seller")
                try:
                    seller_id = int(self._get_input("  Seller ID     : "))
                    name      = self._get_input("  Name          : ")
                    shift     = self._get_input("  Shift (Morning/Afternoon/Night): ")
                    seller = Seller(seller_id, name, shift)
                    self.system.register_seller(seller)
                except ValueError:
                    print("  [!] Invalid input.")

            elif choice == "2":
                self._print_header("Seller Rotation")
                self.system.seller_rotation.display()

            elif choice == "3":
                self._print_header("Next Seller")
                self.system.assign_next_seller()

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    def sales_menu(self):
        """Sub-menu for sales operations."""
        while True:
            self._print_header("SALES MANAGEMENT")
            print("  1. Process new sale")
            print("  2. View sales history")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Process Sale")
                try:
                    cust_id   = int(self._get_input("  Customer ID   : "))
                    book_idx  = int(self._get_input("  Book index in catalog (0-based): "))
                    quantity  = int(self._get_input("  Quantity      : "))

                    # Walk the singly linked list to find the customer by ID
                    customer = None
                    current = self.system.customer_registry.head
                    while current:
                        if current.data.customer_id == cust_id:
                            customer = current.data
                            break
                        current = current.next

                    book     = self.system.book_catalog.get(book_idx)
                    seller   = self.system.seller_rotation.get_next()

                    if not customer:
                        print(f"  [!] Customer ID {cust_id} not found.")
                    elif not book:
                        print(f"  [!] No book at index {book_idx}.")
                    elif not seller:
                        print("  [!] No sellers registered.")
                    else:
                        self.system.process_sale(customer, book, seller, quantity)
                except ValueError:
                    print("  [!] Invalid input. Please enter numeric values.")

            elif choice == "2":
                self._print_header("Sales History")
                self.system.view_sales_history()

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    def returns_menu(self):
        """Sub-menu for cancellation and return operations."""
        while True:
            self._print_header("RETURNS & CANCELLATIONS")
            print("  1. Cancel most recent sale (push to stack)")
            print("  2. Process return (pop from stack)")
            print("  3. View cancellation stack")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Cancel Sale")
                sale = self.system.get_last_sale()
                if sale:
                    self.system.cancel_sale(sale)
                else:
                    print("  No sales recorded to cancel.")

            elif choice == "2":
                self._print_header("Process Return")
                self.system.process_return()

            elif choice == "3":
                self._print_header("Cancellation Stack")
                self.system.view_canceled_sales()

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    def promotions_menu(self):
        """Sub-menu for weekly promotion navigation."""
        while True:
            self._print_header("WEEKLY PROMOTIONS")
            print("  1. Add new promotion")
            print("  2. Navigate forward  [>>]")
            print("  3. Navigate backward [<<]")
            print("  4. View current promotion")
            print("  5. View all promotions")
            print("  0. Back")
            self._print_separator()
            choice = self._get_input("Select an option: ")

            if choice == "1":
                self._print_header("Add Promotion")
                try:
                    promo_id   = int(self._get_input("  Promotion ID      : "))
                    name       = self._get_input("  Name              : ")
                    discount   = float(self._get_input("  Discount (%)      : "))
                    active_day = self._get_input("  Active day (e.g. Monday): ")
                    promo = Promotion(promo_id, name, discount, active_day)
                    self.system.add_promotion(promo)
                except ValueError:
                    print("  [!] Invalid input.")

            elif choice == "2":
                self._print_header("Next Promotion")
                self.system.next_promotion()

            elif choice == "3":
                self._print_header("Previous Promotion")
                self.system.previous_promotion()

            elif choice == "4":
                self._print_header("Current Promotion")
                self.system.view_current_promotion()

            elif choice == "5":
                self._print_header("All Promotions")
                self.system.promotions.display()

            elif choice == "0":
                break
            else:
                print("  [!] Invalid option.")

            self._print_separator()

    # -----------------------------------------------------------------------
    # Helper methods
    # -----------------------------------------------------------------------

    def _get_input(self, prompt: str) -> str:
        """Helper for validated, stripped user input."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return "0"

    def _print_header(self, title: str):
        """Helper for formatted section headers."""
        print()
        print("=" * 50)
        print(f"  {title}")
        print("=" * 50)

    def _print_separator(self):
        """Helper for visual dividers between sections."""
        print("-" * 50)
