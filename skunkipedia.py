import os
import sys
import time
import msvcrt
import pyperclip
try:
    import msvcrt 
except ImportError:
    msvcrt = None

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

COST_CENTERS = {
    "728": {
        "Department": "Library Services (Library)",
        "Location": "325 Avenue A NW, Winter Haven, FL 33881",
        "Contact": "Jane Martin, jmartin@mywinterhaven.com, 333-333-3333",
    },

    "923": {
        "Department": "Technology Services (Nora Mayo Hall, City Hall Annex)",
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881, Nora Mayo Hall - 800 Ave A NW, Winter Haven, FL 33881",
        "Contact": "Hiep Nguyen, hnguyen@mywinterhaven.com, 333-333-3333",
    },

    "618": {
        "Department": "Water Department Customer Service", 
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881", 
        "Contact": "Gabby Gardner, ggardner@mywinterhaven.com, 863-291-5678 x 3370",
    },

    "111": {
        "Department": "Finance Department",
        "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Coleen \"CJ\" Scott (CFO), cjscott@mywinterhaven.com, 863-291-5667 x 2500" 
    }
}

WINDOWS_11_KEY = "MVHNP-G8632-B482B-QDW8D-QRR8R"
WINDOWS_10_KEY = "MVHNP-G8632-B482B-QDW8D-QRR8R"
WINDOWS_8_1_KEY = "MPXWC-7CN4B-64FCB-9T69B-F9BDQ"
WINDOWS_7_KEY = "YTH8H-3VJ37-T3RVT-YH7HG-KCVPD"


# clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# pause til keypress
def pause(msg="Press any key to continue..."):
    print(msg, end='', flush=True)
    if msvcrt:
        msvcrt.getch()
    else:
        # for some reason it wouldnt work without a fallback
        input()
    print()


def display_home():
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
    print("3) Guides")
    print("4) Troubleshooting")
    print("0) Exit")
    choice = input("\nSelect an option: ").strip()
    return choice


def displayCostCenters():
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



# def displayActivationKeys():
#     #main menu options
#     clear_screen()
#     print("SKUNKIPEDIA - Main Menu")
#     print("=" * 26)
#     print("1) Cost Centers")
#     print("2) Windows Activation Key")
#     print("3) Guides")
#     print("4) Troubleshooting")
#     print("0) Exit")
#     choice = input("\nSelect an option: ").strip()
#     return choice
# def show_cost_center(cc_number):
#     """Display details for a single cost center."""
#     clear_screen()
#     data = COST_CENTERS.get(cc_number)
#     if not data:
#         print("Invalid cost center number.")
#     else:
#         print(f"Cost Center: {cc_number}")
#         print("-" * 30)
#         print(f"Department           : {data['Department']}")
#         print(f"Location             : {data['Location']}")
#         print(f"Primary Contact      : {data['Contact']}")
#     print()
#     pause()


# def show_activation_key():

#     # windows 11
#     clear_screen()
#     print("Windows 11 Activation Key")
#     print("=" * 23)
#     print(WINDOWS_11_KEY)
#     if CLIPBOARD_AVAILABLE:
#         pyperclip.copy(WINDOWS_11_KEY)
#         print("\n[Windows 11 key has been copied to the clipboard.]\n")
#     print()

#     print("Windows 10 Activation Key")
#     print("=" * 23)
#     print(WINDOWS_10_KEY)
#     if CLIPBOARD_AVAILABLE:
#         pyperclip.copy(WINDOWS_10_KEY)
#         print("\n[Windows 10 key has been copied to the clipboard.]\n")
#     print()

#     print("Windows 8.1 Activation Key\n")
#     print("=" * 23)
#     print(WINDOWS_8_1_KEY)
#     if CLIPBOARD_AVAILABLE:
#         pyperclip.copy(WINDOWS_8_1_KEY)
#         print("\n[Windows 8.1 key has been copied to the clipboard.]\n")
#     print()

#     print("Windows 7 Activation Key\n")
#     print("=" * 23)
#     print(WINDOWS_7_KEY)
#     if CLIPBOARD_AVAILABLE:
#         pyperclip.copy(WINDOWS_7_KEY)
#         print("\n[Windows 7 key has been copied to the clipboard.]\n")
#     print()

#     pause()

def displayActivationKeyMenu():
    clear_screen()
    print("Windows Activation Keys")
    print("=" * 23)
    print("1) Windows 11")
    print("2) Windows 10")
    print("3) Windows 8.1")
    print("4) Windows 7")
    print("0) Back")
    choice = input("\nSelect an option: ").strip()
    return choice

def showActivationKey(version):
    clear_screen()
    if version == "1":
        print("Windows 11 Activation Key", WINDOWS_11_KEY")
    elif version == "2":
        print("Windows 10 Activation Key", WINDOWS_10_KEY")
    elif version == "3":
        print("Windows 8.1 Activation Key", WINDOWS_8_1_KEY")
    elif version == "4":
        print("Windows 7 Activation Key", WINDOWS_7_KEY")
    else:
        print("Invalid selection.")
        pause()
        return


        
    




def main():
    display_home()
    while True:
        choice = display_main_menu()
        if choice == "1":
            # Cost Centers
            while True:
                cc_choice = displayCostCenters()
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

# how to build?
# do it in howard -
#  pyinstaller --onefile skunkipedia.py --distpath "\\\\howard\\01 - Technology Services\\11 - Training"

# do it in the github folder
# pyinstaller --onefile skunkipedia.py (can't already be open)

