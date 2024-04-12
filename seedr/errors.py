"""
Module for custom Errors
"""



class InvalidEmailError(Exception):
    """
    Exception raised for invalid email format.

    Attributes:
        email -- input email which caused the error
        message -- explanation of the error
    """

    def __init__(self, email, message="Invalid email"):
        self.email = email
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.email} is an {self.message}"
