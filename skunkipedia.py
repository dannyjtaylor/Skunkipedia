#!/usr/bin/env python3
"""
Skunkipedia CLI
A simple interactive dictionary for the IT department to look up cost centers
and the Windows Activation Key. 

Author: Your Name
Date:   2025-08-07
"""

import os
import sys
import time

# Windows-specific modules
try:
    import msvcrt  # for press-any-key on Windows
except ImportError:
    msvcrt = None

# Optional clipboard support
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

# -------------------------------------------------------------------
# Data Definitions
# -------------------------------------------------------------------
COST_CENTERS = {
    "728": {
        "Department": "Library Services (Library)",
        "Location": "325 Avenue A NW, Winter Haven, FL 33881",
        "Contact": "Jane Martin, jmartin@mywinterhaven.com, 333-333-3333",
    },
    "923": {
        "Department": "Technology Services (Nora Mayo Hall, City Hall Annex)",
        "Location": "451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Hiep Nguyen, hnguyen@mywinterhaven.com, 333-333-3333",
    }
}

WINDOWS_KEY = "39391-239291-29291"


# -------------------------------------------------------------------
# Utility Functions
# -------------------------------------------------------------------
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(msg="Press any key to continue..."):
    """Pause until user presses a key (Windows only)."""
    print(msg, end='', flush=True)
    if msvcrt:
        msvcrt.getch()
    else:
        input()  # fallback
    print()  # newline after keypress


# -------------------------------------------------------------------
# Display Functions
# -------------------------------------------------------------------
def display_home():
    """Show the ASCII-art home screen."""
    clear_screen()
    banner = r"""
 _____ _                _    _                _ _       
/  ___| |              | |  (_)              | (_)      
\ `--.| | ___   _ _ __ | | ___ _ __   ___  __| |_  __ _ 
 `--. \ |/ / | | | '_ \| |/ / | '_ \ / _ \/ _` | |/ _` |
/\__/ /   <| |_| | | | |   <| | |_) |  __/ (_| | | (_| |
\____/|_|\_\\__,_|_| |_|_|\_\_| .__/ \___|\__,_|_|\__,_|
                              | |                       
                              |_|                       
    """
    bigfoot = r"""
       _...._
     .-.     /
    /o.o\ ):.\
    \   / `- .`--._
    // /            `-.
   '...\     .         `.
    `--''.    '          `.
        .'   .'            `-.
     .-'    /`-.._            \
   .'    _.'      :      .-'"'/
  | _,--`       .'     .'    /
  \ \          /     .'     /
   \///        |    ' |    /
               \   (  `.   ``-.
                \   \   `._    \
              _.-`   )    .'    )
              `.__.-'  .-' _-.-'
                       `.__,'
    """
    print(banner)
    print("Welcome to SKUNKIPEDIA!")
    print("\nA quick-reference IT dictionary.\n")
    print(bigfoot)
    print()
    pause()


def display_main_menu():
    #main menu options
    clear_screen()
    print("SKUNKIPEDIA - Main Menu")
    print("=" * 26)
    print("1) Cost Centers")
    print("2) Windows Activation Key")
    print("0) Exit")
    choice = input("\nSelect an option: ").strip()
    return choice


def display_cost_centers_menu():
    #show the cost centers submenu
    clear_screen()
    print("Cost Centers")
    print("=" * 12)
    for cc in COST_CENTERS:
        dept = COST_CENTERS[cc]["Department"]
        print(f"{cc}) {dept}")
    print("0) Back")
    choice = input("\nEnter cost center number: ").strip()
    return choice


def show_cost_center(cc_number):
    """Display details for a single cost center."""
    clear_screen()
    data = COST_CENTERS.get(cc_number)
    if not data:
        print("Invalid cost center number.")
    else:
        print(f"Cost Center: {cc_number}")
        print("-" * 30)
        print(f"Department           : {data['Department']}")
        print(f"Location             : {data['Location']}")
        print(f"Primary Contact      : {data['Contact']}")
    print()
    pause()


def show_activation_key():
    """Display the Windows activation key and copy to clipboard."""
    clear_screen()
    print("Windows Activation Key")
    print("=" * 23)
    print(WINDOWS_KEY)
    if CLIPBOARD_AVAILABLE:
        pyperclip.copy(WINDOWS_KEY)
        print("\n[Key has been copied to your clipboard!]")
    else:
        print("\n(To enable auto-copy, install pyperclip: pip install pyperclip)")
    print()
    pause()


# -------------------------------------------------------------------
# Main Application Loop
# -------------------------------------------------------------------
def main():
    display_home()
    while True:
        choice = display_main_menu()
        if choice == "1":
            # Cost Centers
            while True:
                cc_choice = display_cost_centers_menu()
                if cc_choice == "0":
                    break
                show_cost_center(cc_choice)
        elif choice == "2":
            # Windows Activation Key
            show_activation_key()
        elif choice == "0":
            clear_screen()
            print("Goodbye!")
            time.sleep(0.5)
            sys.exit(0)
        else:
            print("Invalid selection. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    main()

# -------------------------------------------------------------------
# Build Instructions
# -------------------------------------------------------------------
# To create a standalone .exe in your network folder, run:
#   pyinstaller --onefile skunkipedia.py \
#       --distpath "\\\\howard\\01 - Technology Services\\11 - Training"
#
# Requirements:
#  - Python 3.6+
#  - (Optional) pyperclip for clipboard support: pip install pyperclip
#  - PyInstaller: pip install pyinstaller
