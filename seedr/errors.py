"""
Module for custom Errors
"""

import requests


def reset_password(email: str, timeout=10) -> None:
    """
    Sends a password reset request to the Seedr API.

    Args:
        email (str): The email address associated with the account.
        timeout (int, optional): The timeout for the HTTP request in seconds. Defaults to 10.
    """
    response = requests.post(
        "https://www.seedr.cc/auth/password-recover/request",
        data={"email": email},
        timeout=timeout,
    )
    if response.ok:
        print("Password recovery email has been sent")


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
