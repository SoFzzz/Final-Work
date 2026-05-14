# backend/models.py
# Domain model classes for the Library Management System.
# Defines the core entities that represent the real-world objects in the bookstore.



class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, book_id: int, title: str, author: str, genre: str, year: int, price: float, stock: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Book[{self.book_id}] - '{self.title}' by {self.author} ({self.year}) | Genre: {self.genre} | Price: ${self.price:.2f} | Stock: {self.stock}"

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title={self.title!r}, author={self.author!r}, genre={self.genre!r}, year={self.year}, price={self.price}, stock={self.stock})"




class Customer:
    """
    Represents a customer of the library.
    """
    def __init__(self, customer_id: int, name: str, phone: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Customer[{self.customer_id}] - {self.name} | Phone: {self.phone} | Email: {self.email}"

    def __repr__(self):
        return f"Customer(customer_id={self.customer_id}, name={self.name!r}, phone={self.phone!r}, email={self.email!r})"




class Seller:
    """
    Represents a seller (staff member) in the library.
    """
    def __init__(self, seller_id: int, name: str, shift: str, sales_count: int = 0):
        self.seller_id = seller_id
        self.name = name
        self.shift = shift
        self.sales_count = sales_count

    def __str__(self):
        return f"Seller[{self.seller_id}] - {self.name} | Shift: {self.shift} | Sales: {self.sales_count}"

    def __repr__(self):
        return f"Seller(seller_id={self.seller_id}, name={self.name!r}, shift={self.shift!r}, sales_count={self.sales_count})"




class Sale:
    """
    Represents a sale transaction in the library.
    """
    def __init__(self, sale_id: int, customer: 'Customer', seller: 'Seller', book: 'Book', quantity: int, total_price: float, date: str = "", status: str = "Completed"):
        self.sale_id = sale_id
        self.customer = customer
        self.seller = seller
        self.book = book
        self.quantity = quantity
        self.total_price = total_price
        self.date = date
        self.status = status

    def __str__(self):
        return (
            f"Sale[{self.sale_id}] - Customer: {self.customer.name} | "
            f"Seller: {self.seller.name} | Book: '{self.book.title}' | "
            f"Quantity: {self.quantity} | Total: ${self.total_price:.2f} | Date: {self.date} | Status: {self.status}"
        )

    def __repr__(self):
        return f"Sale(sale_id={self.sale_id}, customer={self.customer!r}, seller={self.seller!r}, book={self.book!r}, quantity={self.quantity}, total_price={self.total_price}, date={self.date!r}, status={self.status!r})"




class Promotion:
    """
    Represents a promotion available in the library.
    """
    def __init__(self, promotion_id: int, name: str, discount_percentage: float, active_day: str):
        self.promotion_id = promotion_id
        self.name = name
        self.discount_percentage = discount_percentage
        self.active_day = active_day

    def __str__(self):
        return (
            f"Promotion[{self.promotion_id}] - {self.name} | "
            f"Discount: {self.discount_percentage}% | Active Day: {self.active_day}"
        )

    def __repr__(self):
        return f"Promotion(promotion_id={self.promotion_id}, name={self.name!r}, discount_percentage={self.discount_percentage}, active_day={self.active_day!r})"
