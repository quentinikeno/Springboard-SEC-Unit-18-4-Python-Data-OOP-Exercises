"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Set the starting number to be 'start'"""
        self.start = start
        self.current = start

    def __repr__(self):
        """Return representation of SerialGenerator instance."""
        return f"<SerialGenerator start = {self.start}>"

    def generate(self):
        """Add 1 to the current number and return the updated current number"""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Reset the current number back to the original start number."""
        self.current = self.start