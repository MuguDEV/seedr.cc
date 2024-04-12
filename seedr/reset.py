"""
Module for resetting password 
"""

import requests
from .errors import InvalidEmailError


def reset_password(email: str) -> None:
    """
    Sends a password reset request to the Seedr API.

    Args:
        email (str): The email address associated with the account.
    """
    response = requests.post(
        "https://www.seedr.cc/auth/password-recover/request",
        data={"email": email},
        timeout=10,
    ).json()
    if response.get("success", 0):
        print("Password recovery email has been sent")
    elif response.get("code", "") == "401":
        raise InvalidEmailError(email)
