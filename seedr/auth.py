"""Module for authentication functionality"""

from typing import Dict, NamedTuple
import requests


class Data(NamedTuple):
    """
    Represents user response retrieved from the API.
    """

    new_user: bool
    username: str
    email: str
    user_id: int
    is_premium: bool
    access_token: str
    expires_in: str
    refresh_token: str
    success: bool
    cookie: str


def login(username: str, password: str) -> Data:
    """
    Logs in a user and retrieves user response.

    Args:
        username (str): The username for login.
        password (str): The password for login.

    Returns:
        Data: A named tuple containing user response.
    """
    response: Dict = requests.post(
        "https://www.seedr.cc/auth/login",
        data={
            "username": username,
            "password": password,
            "g-recaptcha-response": "",
            "h-recaptha-response": "",
        },
        timeout=10,
    ).json()

    return Data(
        new_user=response.get("new_user", False),
        username=response.get("username", ""),
        email=response.get("email", ""),
        user_id=response.get("user_id", 0),
        is_premium=response.get("is_premium", False),
        access_token=response.get("access_token", ""),
        expires_in=response.get("expires_in", ""),
        refresh_token=response.get("refresh_token", ""),
        success=response.get("success", False),
        cookies=response.get("cookies", "")[0].split(";")[0],
    )
