"""
=========================================
NetSpectre Banner
=========================================
"""

from core.colors import Colors
from core.constants import APP_NAME, VERSION, AUTHOR, TAGLINE


def show_banner():
    """
    Display the NetSpectre startup banner.
    """

    print(Colors.TITLE + "=" * 72)

    print(Colors.SUCCESS + r"""
 _   _      _    ____                  _____                 _             
| \ | | ___| |_ / ___| _ __   ___  ___| ____|_   _____ _ __ | |_ ___ _ __  
|  \| |/ _ \ __|\___ \| '_ \ / _ \/ __|  _| \ \ / / _ \ '_ \| __/ _ \ '__| 
| |\  |  __/ |_  ___) | |_) |  __/ (__| |___ \ V /  __/ | | | ||  __/ |    
|_| \_|\___|\__||____/| .__/ \___|\___|_____| \_/ \___|_| |_|\__\___|_|    
                      |_|                                                   
""")

    print(Colors.INFO + APP_NAME)
    print(Colors.SUCCESS + "Professional Network Reconnaissance Framework")

    print(Colors.WARNING + f"Version : {VERSION}")
    print(Colors.WARNING + f"Author  : {AUTHOR}")

    print(Colors.INFO + TAGLINE)

    print(Colors.TITLE + "=" * 72)

    print(Colors.RESET)
