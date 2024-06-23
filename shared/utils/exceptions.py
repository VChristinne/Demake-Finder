"""
Expections for the shared module to be used in the other modules.
"""

class InvalidInputError(Exception):
    """
    Exception raised for invalid input
    """
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)

class InvalidArgumentError(Exception):
    """
    Exception raised for invalid argument
    """
    def __init__(self, message="Invalid argument"):
        self.message = message
        super().__init__(self.message)

class InvalidDirectoryError(Exception):
    """
    Exception raised for invalid directory
    """
    def __init__(self, message="Invalid directory"):
        self.message = message
        super().__init__(self.message)

class FileNotFoundError(Exception):
    """
    Exception raised for file not found
    """
    def __init__(self, message="File not found"):
        self.message = message
        super().__init__(self.message)

class PermissionDeniedError(Exception):
    """
    Exception raised for permission denied
    """
    def __init__(self, message="Permission denied"):
        self.message = message
        super().__init__(self.message)

class UnknownError(Exception):
    """
    Exception raised for unknown error
    """
    def __init__(self, message="Unknown error"):
        self.message = message
        super().__init__(self.message)
