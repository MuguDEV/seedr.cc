"""
This module is used to fetch settings of seedr.cc account 🌱
"""

from typing import NamedTuple, List, Dict
import requests


class Settings(NamedTuple):
    """
    Represents user settings retrieved from the Seedr API.
    """

    allow_remote_access: bool
    site_language: str
    subtitles_language: str
    email_announcements: bool
    email_newsletter: bool
    username: str
    email: str
    user_id: int
    premium: bool
    space_used: int
    space_max: int
    bandwidth_used: int
    package_id: int
    package_name: str
    wishlist: List[Dict[str, any]]
    invites: int
    invites_accepted: int
    country: str


def get_settings(cookie_str: str, timeout: int = 10) -> Settings:
    """
    Retrieves user settings from the Seedr API.

    Args:
        cookie_str (str): The cookie string used for authentication.


    Returns:
        Settings: A named tuple containing user settings.
    """
    response = requests.get(
        "https://www.seedr.cc/account/settings",
        headers={"Cookie": cookie_str},
        timeout=timeout,
    ).json()

    account = response.get("account", {})
    settings = response.get("settings", {})

    return Settings(
        allow_remote_access=settings.get("allow_remote_access", False),
        site_language=settings.get("site_language", ""),
        subtitles_language=settings.get("subtitles_language", ""),
        email_announcements=settings.get("email_announcements", False),
        email_newsletter=settings.get("email_newsletter", False),
        username=account.get("username", ""),
        email=account.get("email", ""),
        user_id=account.get("user_id", 0),
        premium=account.get("premium", False),
        space_used=account.get("space_used", 0),
        space_max=account.get("space_max", 0),
        bandwidth_used=account.get("bandwidth_used", 0),
        package_id=account.get("package_id", 0),
        package_name=account.get("package_name", ""),
        wishlist=account.get("wishlist", []),
        invites=account.get("invites", 0),
        invites_accepted=account.get("invites_accepted", 0),
        country=response.get("country", ""),
    )
