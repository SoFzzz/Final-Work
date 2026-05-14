"""
Simple List Data Structure

Purpose: Store the book catalog
This structure manages a linear sequential collection of items.
"""


class SimpleList:
    """
    A managed custom list implementation for storing sequential data.
    
    Use Case: Store the complete book catalog in the library system.
    Internally uses a Python list to manage the items.
    """
    
    def __init__(self):
        """Initialize an empty simple list."""
        self.items = []
    
    def add(self, item):
        """
        Add an item to the end of the list.
        
        Args:
            item: The item to be added to the list
            
        Returns:
            bool: True if the item was added successfully
        """
        if item is None:
            raise ValueError("Cannot add None as an item")
        
        self.items.append(item)
        return True
    
    def remove(self, item):
        """
        Remove the first occurrence of an item from the list.
        
        Args:
            item: The item to remove
            
        Returns:
            bool: True if the item was removed, False if not found
        """
        if item not in self.items:
            return False
        
        self.items.remove(item)
        return True
    
    def search(self, item):
        """
        Search for an item in the list.
        
        Args:
            item: The item to search for
            
        Returns:
            int: The index of the item if found, -1 otherwise
        """
        try:
            return self.items.index(item)
        except ValueError:
            return -1
    
    def update(self, index, new_item):
        """
        Update an item at a specific index.
        
        Args:
            index: The index of the item to update
            new_item: The new item value
            
        Returns:
            bool: True if the update was successful, False otherwise
            
        Raises:
            IndexError: If the index is out of range
        """
        if new_item is None:
            raise ValueError("Cannot set item to None")
        
        if index < 0 or index >= len(self.items):
            raise IndexError(f"Index {index} is out of range")
        
        self.items[index] = new_item
        return True
    
    def get_all(self):
        """
        Get all items in the list.
        
        Returns:
            list: A copy of all items in the list
        """
        return self.items.copy()
    
    def is_empty(self):
        """
        Check if the list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self):
        """
        Get the total number of items in the list.
        
        Returns:
            int: The number of items currently in the list
        """
        return len(self.items)
    
    def __str__(self):
        """
        String representation of the list.
        
        Returns:
            str: A readable string representation of the list
        """
        return f"SimpleList({self.items})"
    
    def __repr__(self):
        """
        Developer-friendly representation of the list.
        
        Returns:
            str: A detailed representation of the list
        """
        return f"SimpleList(size={self.size()}, items={self.items})"


if __name__ == "__main__":
    # Usage example: Book Catalog
    print("=" * 60)
    print("SIMPLE LIST - BOOK CATALOG EXAMPLE")
    print("=" * 60)
    
    # Create a simple list for book catalog
    catalog = SimpleList()
    
    # Add some books
    books = [
        "The Great Gatsby - F. Scott Fitzgerald",
        "1984 - George Orwell",
        "Pride and Prejudice - Jane Austen",
        "To Kill a Mockingbird - Harper Lee"
    ]
    
    print("\n1. Adding books to the catalog:")
    for book in books:
        catalog.add(book)
        print(f"   ✓ Added: {book}")
    
    # Display all books
    print(f"\n2. Total books in catalog: {catalog.size()}")
    print("   Books in catalog:")
    for idx, book in enumerate(catalog.get_all()):
        print(f"   [{idx}] {book}")
    
    # Search for a book
    search_title = "1984 - George Orwell"
    position = catalog.search(search_title)
    print(f"\n3. Search for '{search_title}':")
    print(f"   Found at index: {position}")
    
    # Update a book
    print("\n4. Updating a book:")
    print(f"   Before: {catalog.get_all()[0]}")
    catalog.update(0, "The Great Gatsby - F. Scott Fitzgerald (2nd Edition)")
    print(f"   After:  {catalog.get_all()[0]}")
    
    # Remove a book
    print("\n5. Removing a book:")
    removed_book = "Pride and Prejudice - Jane Austen"
    if catalog.remove(removed_book):
        print(f"   ✓ Removed: {removed_book}")
    
    # Check if empty
    print(f"\n6. Is catalog empty? {catalog.is_empty()}")
    print(f"   Current size: {catalog.size()}")
    
    # Display final state
    print("\n7. Final catalog state:")
    for idx, book in enumerate(catalog.get_all()):
        print(f"   [{idx}] {book}")
    
    print("\n" + "=" * 60)
