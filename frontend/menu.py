import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from backend.library_system import LibrarySystem
from backend.models import Book, Customer, Seller, Promotion

class BookstoreDashboard:
    """Graphical User Interface for the Library Management System.
    Replaces the old CLI menu with a modern, componentized Tkinter dashboard.
    """
    def __init__(self, system: LibrarySystem):
        self.system = system
        self.root = tk.Tk()
        self.root.title("Library Management System - Dashboard")
        self.root.geometry("900x600")
        self._configure_styles()
        self._build_layout()

    def _configure_styles(self):
        style = ttk.Style()
        # Use a cleaner theme if available (clam is usually cross-platform)
        if 'clam' in style.theme_names():
            style.theme_use('clam')
        
        style.configure('TNotebook.Tab', padding=[15, 5], font=('Segoe UI', 10, 'bold'))
        style.configure('TButton', font=('Segoe UI', 10), padding=5)
        style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'))

    def _build_layout(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=15, pady=15)

        self._build_book_catalog_tab()
        self._build_customer_registry_tab()
        self._build_seller_roster_tab()
        self._build_sales_terminal_tab()
        self._build_returns_tab()
        self._build_promotions_hub_tab()

    def _create_form(self, title, fields, on_submit_callback):
        """Helper to dynamically generate input forms (DRY principle)."""
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.grab_set() # Make it modal
        
        entries = {}
        for idx, field in enumerate(fields):
            ttk.Label(dialog, text=field).grid(row=idx, column=0, padx=10, pady=5, sticky='w')
            entry = ttk.Entry(dialog, width=30)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entries[field] = entry

        def handle_submit():
            values = {f: e.get() for f, e in entries.items()}
            # callback returns True if successful to close dialog
            if on_submit_callback(values):
                dialog.destroy()

        ttk.Button(dialog, text="Submit", command=handle_submit).grid(row=len(fields), column=0, columnspan=2, pady=15)

    def _create_listbox_with_scroll(self, parent):
        """Helper to create a listbox with a vertical scrollbar."""
        frame = ttk.Frame(parent)
        frame.pack(fill='both', expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        
        listbox = tk.Listbox(frame, font=('Consolas', 10), yscrollcommand=scrollbar.set)
        listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=listbox.yview)
        
        return listbox

    # -----------------------------------------------------------------------
    # Book Catalog Tab
    # -----------------------------------------------------------------------
    def _build_book_catalog_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Book Catalog")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')

        ttk.Button(btn_frame, text="Register New Book", command=self._register_book).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Search Book", command=self._search_book).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh Catalog", command=self._refresh_books).pack(side='left', padx=5)

        self.book_listbox = self._create_listbox_with_scroll(frame)
        self._refresh_books()

    def _register_book(self):
        fields = ['Book ID', 'Title', 'Author', 'Genre', 'Year', 'Price ($)', 'Stock']
        
        def on_submit(values):
            try:
                book = Book(
                    int(values['Book ID']), values['Title'], values['Author'],
                    values['Genre'], int(values['Year']), float(values['Price ($)']),
                    int(values['Stock'])
                )
                self.system.register_book(book)
                messagebox.showinfo("Success", f"Book '{book.title}' registered successfully!")
                self._refresh_books()
                return True
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric data format.")
                return False

        self._create_form("Register Book", fields, on_submit)

    def _refresh_books(self):
        self.book_listbox.delete(0, tk.END)
        for i in range(self.system.book_catalog.size()):
            self.book_listbox.insert(tk.END, str(self.system.book_catalog.get(i)))

    def _search_book(self):
        query = simpledialog.askstring("Search Book", "Enter title or author:")
        if not query: return
        
        query_lower = query.lower()
        self.book_listbox.delete(0, tk.END)
        
        found = False
        for i in range(self.system.book_catalog.size()):
            book = self.system.book_catalog.get(i)
            if query_lower in book.title.lower() or query_lower in book.author.lower():
                self.book_listbox.insert(tk.END, str(book))
                found = True
                
        if not found:
            self.book_listbox.insert(tk.END, "No books found.")

    # -----------------------------------------------------------------------
    # Customer Registry Tab
    # -----------------------------------------------------------------------
    def _build_customer_registry_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Customer Registry")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')

        ttk.Button(btn_frame, text="Register Customer", command=self._register_customer).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Enqueue Customer", command=self._enqueue_customer).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Attend Next Customer", command=self._attend_next).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh Queue", command=self._refresh_customer_queue).pack(side='left', padx=5)

        ttk.Label(frame, text="Current Waiting Queue:", font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(10,0))
        self.customer_queue_listbox = self._create_listbox_with_scroll(frame)

    def _register_customer(self):
        fields = ['Customer ID', 'Name', 'Phone', 'Email']
        
        def on_submit(values):
            try:
                customer = Customer(
                    int(values['Customer ID']), values['Name'],
                    values['Phone'], values['Email']
                )
                self.system.register_customer(customer)
                messagebox.showinfo("Success", "Customer registered successfully!")
                return True
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric data format.")
                return False

        self._create_form("Register Customer", fields, on_submit)

    def _enqueue_customer(self):
        cust_id_str = simpledialog.askstring("Enqueue", "Enter Customer ID to enqueue:")
        if not cust_id_str: return
        
        try:
            cust_id = int(cust_id_str)
            found = None
            current = self.system.customer_registry.head
            while current:
                if current.data.customer_id == cust_id:
                    found = current.data
                    break
                current = current.next
                
            if found:
                self.system.add_customer_to_queue(found)
                messagebox.showinfo("Success", f"{found.name} added to the waiting queue!")
                self._refresh_customer_queue()
            else:
                messagebox.showerror("Error", "Customer ID not found in registry.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric ID.")

    def _attend_next(self):
        result = self.system.attend_next_customer()
        if result:
            customer, seller = result
            messagebox.showinfo("Attending Customer", f"Now Attending: {customer.name}\nAssigned Seller: {seller.name}")
        else:
            messagebox.showwarning("Notice", "The queue is empty or no sellers are available.")
        self._refresh_customer_queue()

    def _refresh_customer_queue(self):
        self.customer_queue_listbox.delete(0, tk.END)
        for i in range(self.system.customer_queue.size()):
            self.customer_queue_listbox.insert(tk.END, str(self.system.customer_queue.items[i]))

    # -----------------------------------------------------------------------
    # Seller Roster Tab
    # -----------------------------------------------------------------------
    def _build_seller_roster_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Seller Roster")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame, text="Register Seller", command=self._register_seller).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Test Next Rotation", command=self._next_rotation).pack(side='left', padx=5)

        ttk.Label(frame, text="Seller Rotation Cycle:", font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(10,0))
        self.seller_listbox = self._create_listbox_with_scroll(frame)

    def _register_seller(self):
        fields = ['Seller ID', 'Name', 'Shift (Morning/Evening)']
        
        def on_submit(values):
            try:
                seller = Seller(int(values['Seller ID']), values['Name'], values['Shift (Morning/Evening)'])
                self.system.register_seller(seller)
                messagebox.showinfo("Success", "Seller added to rotation!")
                self._refresh_sellers()
                return True
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric data format.")
                return False

        self._create_form("Register Seller", fields, on_submit)

    def _next_rotation(self):
        seller = self.system.assign_next_seller()
        if seller:
            messagebox.showinfo("Rotation Next", f"The next seller in rotation is: {seller.name}")
        else:
            messagebox.showwarning("Notice", "No sellers are currently registered.")
        self._refresh_sellers()

    def _refresh_sellers(self):
        self.seller_listbox.delete(0, tk.END)
        if self.system.seller_rotation.is_empty():
            self.seller_listbox.insert(tk.END, "No sellers in rotation.")
            return
            
        node = self.system.seller_rotation.head
        for _ in range(self.system.seller_rotation.size()):
            self.seller_listbox.insert(tk.END, str(node.data))
            node = node.next

    # -----------------------------------------------------------------------
    # Sales Terminal Tab
    # -----------------------------------------------------------------------
    def _build_sales_terminal_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Sales Terminal")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame, text="Process New Sale", command=self._process_sale).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh History", command=self._refresh_sales_history).pack(side='left', padx=5)

        ttk.Label(frame, text="Sales History Log:", font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(10,0))
        self.sales_listbox = self._create_listbox_with_scroll(frame)

    def _process_sale(self):
        fields = ['Customer ID', 'Book Index (0-based in Catalog)', 'Quantity']
        
        def on_submit(values):
            try:
                cust_id = int(values['Customer ID'])
                book_idx = int(values['Book Index (0-based in Catalog)'])
                qty = int(values['Quantity'])

                customer = None
                current = self.system.customer_registry.head
                while current:
                    if current.data.customer_id == cust_id:
                        customer = current.data
                        break
                    current = current.next

                book = self.system.book_catalog.get(book_idx)
                seller = self.system.seller_rotation.get_next()

                if not customer:
                    messagebox.showerror("Error", f"Customer ID {cust_id} not found.")
                    return False
                elif not book:
                    messagebox.showerror("Error", f"No book found at index {book_idx}.")
                    return False
                elif not seller:
                    messagebox.showerror("Error", "No sellers available in rotation.")
                    return False
                
                sale = self.system.process_sale(customer, book, seller, qty)
                if sale:
                    messagebox.showinfo("Success", "Sale processed successfully!")
                    self._refresh_sales_history()
                    return True
                else:
                    messagebox.showwarning("Warning", "Insufficient stock to complete sale.")
                    return False
            except ValueError:
                messagebox.showerror("Error", "All inputs must be numeric integers.")
                return False

        self._create_form("Process Sale", fields, on_submit)

    def _refresh_sales_history(self):
        self.sales_listbox.delete(0, tk.END)
        current = self.system.sales_history.head
        while current:
            self.sales_listbox.insert(tk.END, str(current.data))
            current = current.next

    # -----------------------------------------------------------------------
    # Returns & Cancellations Tab
    # -----------------------------------------------------------------------
    def _build_returns_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Returns & Reversals")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame, text="Cancel Most Recent Sale", command=self._cancel_sale).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Process Return (Pop Stack)", command=self._process_return).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Refresh Reversal Log", command=self._refresh_returns).pack(side='left', padx=5)

        ttk.Label(frame, text="Cancellations Stack:", font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(10,0))
        self.returns_listbox = self._create_listbox_with_scroll(frame)

    def _cancel_sale(self):
        sale = self.system.get_last_sale()
        if sale:
            self.system.cancel_sale(sale)
            messagebox.showinfo("Sale Cancelled", f"Sale #{sale.sale_id} has been cancelled and pushed to stack.")
            self._refresh_returns()
            self._refresh_sales_history()
        else:
            messagebox.showwarning("Notice", "No recent sales found to cancel.")

    def _process_return(self):
        sale = self.system.process_return()
        if sale:
            messagebox.showinfo("Return Processed", f"Stock restored for Sale #{sale.sale_id}.")
            self._refresh_returns()
        else:
            messagebox.showwarning("Notice", "No cancelled sales available to process.")

    def _refresh_returns(self):
        self.returns_listbox.delete(0, tk.END)
        for i in range(self.system.cancellation_stack.top, -1, -1):
            self.returns_listbox.insert(tk.END, str(self.system.cancellation_stack.items[i]))

    # -----------------------------------------------------------------------
    # Promotions Hub Tab
    # -----------------------------------------------------------------------
    def _build_promotions_hub_tab(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Promotions Hub")

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame, text="Register Promotion", command=self._add_promotion).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="<< Previous", command=self._prev_promo).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Next >>", command=self._next_promo).pack(side='left', padx=5)

        self.promo_label = ttk.Label(frame, text="Active Promotion: None", font=('Segoe UI', 14, 'bold'), foreground='blue')
        self.promo_label.pack(pady=20)
        
        ttk.Label(frame, text="All Promotions List:", font=('Segoe UI', 11, 'bold')).pack(anchor='w', pady=(10,0))
        self.promo_listbox = self._create_listbox_with_scroll(frame)

    def _add_promotion(self):
        fields = ['Promotion ID', 'Name', 'Discount (%)', 'Active Day']
        
        def on_submit(values):
            try:
                promo = Promotion(
                    int(values['Promotion ID']), values['Name'],
                    float(values['Discount (%)']), values['Active Day']
                )
                self.system.add_promotion(promo)
                messagebox.showinfo("Success", "Promotion added to circular browser!")
                self._refresh_promotions()
                return True
            except ValueError:
                messagebox.showerror("Error", "Invalid numeric data format.")
                return False

        self._create_form("Register Promotion", fields, on_submit)

    def _next_promo(self):
        promo = self.system.next_promotion()
        if promo: self._refresh_promotions()

    def _prev_promo(self):
        promo = self.system.previous_promotion()
        if promo: self._refresh_promotions()

    def _refresh_promotions(self):
        self.promo_listbox.delete(0, tk.END)
        if self.system.promotions.current:
            self.promo_label.config(text=f"Active Promotion: {self.system.promotions.current.data}")
            
        node = self.system.promotions.head
        if not node: return
        for _ in range(self.system.promotions.size()):
            self.promo_listbox.insert(tk.END, str(node.data))
            node = node.next

    # -----------------------------------------------------------------------
    # Main Application Loop
    # -----------------------------------------------------------------------
    def run(self):
        """Starts the Tkinter main event loop."""
        self.root.mainloop()
