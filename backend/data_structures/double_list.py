"""
Double List Data Structure

Purpose: Store normal prices and discounted prices
This structure manages paired values that must stay synchronized.
"""


class DoubleList:
    """
    A managed custom double list implementation for storing paired data.
    
    Use Case: Store normal prices and discounted prices for books.
    Internally uses tuples to manage paired information.
    """
    
    def __init__(self):
        """Initialize an empty double list."""
        self.pairs = []
    
    def add(self, first_value, second_value):
        """
        Add a pair of values to the double list.
        
        Args:
            first_value: The first value of the pair (e.g., normal price)
            second_value: The second value of the pair (e.g., discounted price)
            
        Returns:
            bool: True if the pair was added successfully
            
        Raises:
            ValueError: If any value is None
        """
        if first_value is None or second_value is None:
            raise ValueError("Cannot add None values to the double list")
        
        # Create a tuple pair and add to list
        pair = (first_value, second_value)
        self.pairs.append(pair)
        return True
    
    def remove(self, index):
        """
        Remove a pair at a specific index.
        
        Args:
            index: The index of the pair to remove
            
        Returns:
            bool: True if the pair was removed successfully
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0 or index >= len(self.pairs):
            raise IndexError(f"Index {index} is out of range")
        
        self.pairs.pop(index)
        return True
    
    def update(self, index, first_value, second_value):
        """
        Update both values of a pair at a specific index.
        
        Args:
            index: The index of the pair to update
            first_value: The new first value
            second_value: The new second value
            
        Returns:
            bool: True if the update was successful
            
        Raises:
            IndexError: If the index is out of range
            ValueError: If any value is None
        """
        if first_value is None or second_value is None:
            raise ValueError("Cannot set values to None")
        
        if index < 0 or index >= len(self.pairs):
            raise IndexError(f"Index {index} is out of range")
        
        self.pairs[index] = (first_value, second_value)
        return True
    
    def search(self, first_value):
        """
        Search for pairs by the first value.
        
        Args:
            first_value: The first value to search for
            
        Returns:
            list: A list of indices where the first value is found
        """
        indices = []
        
        for index, pair in enumerate(self.pairs):
            if pair[0] == first_value:
                indices.append(index)
        
        return indices
    
    def get_all(self):
        """
        Get all pairs in the double list.
        
        Returns:
            list: A copy of all pairs as tuples
        """
        return self.pairs.copy()
    
    def is_empty(self):
        """
        Check if the double list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise
        """
        return len(self.pairs) == 0
    
    def size(self):
        """
        Get the total number of pairs in the double list.
        
        Returns:
            int: The number of pairs currently in the list
        """
        return len(self.pairs)
    
    def get_pair(self, index):
        """
        Get a specific pair at a given index.
        
        Args:
            index: The index of the pair
            
        Returns:
            tuple: The pair (first_value, second_value)
            
        Raises:
            IndexError: If the index is out of range
        """
        if index < 0 or index >= len(self.pairs):
            raise IndexError(f"Index {index} is out of range")
        
        return self.pairs[index]
    
    def get_first_values(self):
        """
        Get all first values from all pairs.
        
        Returns:
            list: A list of all first values
        """
        return [pair[0] for pair in self.pairs]
    
    def get_second_values(self):
        """
        Get all second values from all pairs.
        
        Returns:
            list: A list of all second values
        """
        return [pair[1] for pair in self.pairs]
    
    def __str__(self):
        """
        String representation of the double list.
        
        Returns:
            str: A readable string representation of the double list
        """
        return f"DoubleList({self.pairs})"
    
    def __repr__(self):
        """
        Developer-friendly representation of the double list.
        
        Returns:
            str: A detailed representation of the double list
        """
        return f"DoubleList(size={self.size()}, pairs={self.pairs})"


if __name__ == "__main__":
    # Usage example: Book Prices (Normal and Discounted)
    print("=" * 60)
    print("DOUBLE LIST - BOOK PRICES EXAMPLE")
    print("=" * 60)
    
    # Create a double list for book prices
    prices = DoubleList()
    
    # Add book prices (normal price, discounted price)
    books_prices = [
        ("The Great Gatsby", (15.99, 12.99)),
        ("1984", (18.99, 14.99)),
        ("Pride and Prejudice", (12.99, 9.99)),
        ("To Kill a Mockingbird", (16.99, 13.99))
    ]
    
    print("\n1. Adding book prices (normal and discounted):")
    for book_name, (normal, discount) in books_prices:
        prices.add(book_name, (normal, discount))
        print(f"   ✓ {book_name}: Normal=${normal}, Discount=${discount}")
    
    # Display all prices
    print(f"\n2. Total books in price list: {prices.size()}")
    print("   All book prices:")
    for idx, pair in enumerate(prices.get_all()):
        book, (normal, discount) in (pair[0], pair[1])
        print(f"   [{idx}] {book}: Normal=${normal}, Discount=${discount}")
    
    # Search for a book price
    search_book = "1984"
    found_indices = prices.search(search_book)
    print(f"\n3. Search for '{search_book}':")
    if found_indices:
        for idx in found_indices:
            pair = prices.get_pair(idx)
            print(f"   Found at index {idx}: {pair}")
    
    # Update prices
    print("\n4. Updating book prices:")
    print(f"   Before: {prices.get_pair(0)}")
    prices.update(0, "The Great Gatsby", (15.99, 11.99))
    print(f"   After:  {prices.get_pair(0)}")
    
    # Remove a price entry
    print("\n5. Removing a book price entry:")
    if prices.remove(2):
        print(f"   ✓ Removed price entry at index 2")
    
    # Check if empty
    print(f"\n6. Is price list empty? {prices.is_empty()}")
    print(f"   Current size: {prices.size()}")
    
    # Display all first and second values
    print("\n7. Extract all values:")
    print(f"   All first values: {prices.get_first_values()}")
    print(f"   All second values: {prices.get_second_values()}")
    
    # Display final state
    print("\n8. Final price list state:")
    for idx, pair in enumerate(prices.get_all()):
        book, (normal, discount) = pair[0], pair[1]
        print(f"   [{idx}] {book}: Normal=${normal}, Discount=${discount}")
    
    print("\n" + "=" * 60)
