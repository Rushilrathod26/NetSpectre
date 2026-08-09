"""
NetSpectre Color Engine
Handles all terminal colors used across the project.
"""

from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)


class Colors:

    INFO = Fore.CYAN

    SUCCESS = Fore.GREEN

    WARNING = Fore.YELLOW

    ERROR = Fore.RED

    OPEN = Fore.GREEN

    CLOSED = Fore.RED

    FILTERED = Fore.YELLOW

    DEBUG = Fore.BLUE

    TITLE = Fore.MAGENTA

    RESET = Style.RESET_ALL
