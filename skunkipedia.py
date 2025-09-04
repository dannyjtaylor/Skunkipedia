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
    
def displayGuidesMenu():
    clearScreen()
    print("Guides")
    print("=" * 6)
    for k, v in guides.items():
        print(f"{k}) {v['title']}")
    print("0) Back")
    choice = input("\nSelect a guide: ").strip()
    return choice

def showGuide(guideID):
    clearScreen()
    guide = guides.get(guideID)
    if not guide:
        print("Invalid selection.")
        pause()
        return
    print(guide['title'])
    print("-" * len(guide['title']))
    print(guide['content'])
    print()
    pause()

guides = {
    "1": {
        "title": "How To Verify Security Stack",
        "content": "Step 1: Press the Windows button and type \"addre\" in the Windows Search bar to get to the Add or Remove Programs window.\n\nStep 2: Look for the following programs in the list: \n\t - AutoElevate\n\t - Cortex XDR\n\t - Duo (version 5.1.1)\n\t - Illumio\n\t - NinjaRMM Agent\n\t\nIf you see \"Carbon Black\", note that software should be uninstalled.\n\nStep 3: Please look at the next guide (press 0!)"
    },
    "2": {
        "title": "How To Install/Uninstall Security Stack",
        "content": "Step 1: Navigate to "
    }
}

troubleshooting = {
    "1": {
        "title": "Test",
        "content": "Test2"
    }
}

# costCenters = {
#     "728": {
#         "Department": "Library Services (Library)",
#         "Location": "325 Avenue A NW, Winter Haven, FL 33881",
#         "Contact": "Jane Martin, jmartin@mywinterhaven.com, 333-333-3333",
#     },

#     "923": {
#         "Department": "Technology Services (Nora Mayo Hall, City Hall Annex)",
#         "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881, Nora Mayo Hall - 800 Ave A NW, Winter Haven, FL 33881",
#         "Contact": "Hiep Nguyen, hnguyen@mywinterhaven.com, 333-333-3333",
#     },

#     "618": {
#         "Department": "Water Department Customer Service", 
#         "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881", 
#         "Contact": "Gabby Gardner, ggardner@mywinterhaven.com, 863-291-5678 x 3370",
#     },

#     "111": {
#         "Department": "Finance Department",
#         "Location": "City Hall Annex - 451 3rd St NW, Winter Haven, FL 33881",
#         "Contact": "Coleen \"CJ\" Scott (CFO), cjscott@mywinterhaven.com, 863-291-5667 x 2500" 
#     }
# }

windowsKeys = {
    "1": {
        "name": "Windows 11",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "2": {
        "name": "Windows 10",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "3": {
        "name": "Windows 8.1",
        "key": "MPXWC-7CN4B-64FCB-9T69B-F9BDQ"
    },
    "4": {
        "name": "Windows 7",
        "key": "YTH8H-3VJ37-T3RVT-YH7HG-KCVPD"
    }
}

def displayTroubleshootingMenu():
    clearScreen()
    print("Troubleshooting")
    print("=" * 14)
    for k, v in troubleshooting.items():
        print(f"{k}) {v['title']}")
    print("0) Back")
    choice = input("\nSelect an issue: ").strip()
    return choice

def showTroubleshooting(issue_id):
    clearScreen()
    issue = troubleshooting.get(issue_id)
    if not issue:
        print("Invalid selection.")
        pause()
        return
    print(issue['title'])
    print("-" * len(issue['title']))
    print(issue['content'])
    print()
    pause()

costCenters = {
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
        "Contact": "Coleen \"CJ\" Scott (CFO), cjscott@mywinterhaven.com, 863-291-5667 x 2500", 
    },

    "101": {
        "Department": "City Commission",
        "Location":  "City Manager's Office/Commision - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Bradley T. Dantzler (Mayor), btdantzler@mywinterhaven.com, 863-291-5600 x 224",
    },
    "102": {
        "Department": "Legal",
        "Location": "City Attorney's Office - 245 South Central Ave, Bartow, FL 33830", 
        "Contact": "Frederick John Murlphy, Jr., Esquire (City Attorney), @fjmurphy.com, 863-294-3363", 
    },

    "103": {
        "Department": "City Manager",
        "Location": "City Hall - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "T.Michael Stavres (City Manager), mstavres@mywinterhaven.com, 863-291-5600 x 221",
    },

    "105": {
        "Department": "City Clerk",
        "Location": "City Hall - 451 3rd St NW, Winter Haven, FL 33881",
        "Contact": "Vanessa Castillo (City Clerk), vcastillo@mywinterhaven.com, 863-291-5600 x 224",
    },

    "217": {
        "Department": "Code Compliance",
        "Location": "Fire Station 4 - 1254 Fairfax St NE Winter Haven, FL 33881",
        "Contact": "Ayers Tanya (Code Compliance Supervisor), tayers@mywinterhaven.com, 863-291-5697",
    },

    "200": {
        "Department": "Public Safety - Police",
        "Location": "Police Department - 125 North Lake Silver Drive NW, Winter Haven, FL 33881",
        "Contact": "Vance Monroe (Police Chief), vmonroe@mywinterhaven.com, 863-291-5858",
    },

    "204": {
        "Department": "PAL",
        "Location": "N/A",
        "Contact": "N/A",

    },

    "206": {
        "Department": "Police Grants",
        "Location": "N/A",
        "Contact": "N/A",
    },

    "213": {
        "Department": "Public Safety - Fire Stations",
        "Location": "Fire Station 1 - 301 Avenue G, Winter Haven, FL 33880\n\t\t       Fire Station 2 - 4700 Lucerne Park Rd, Winter Haven, FL 33881\n\t\t       Fire Station 3 - 6975 Eloise Loop Rd, Winter Haven, FL 33884\n\t\t       Fire Station 4 - 1254 Fairfax St NE, Winter Haven, FL 33881\n\t\t       Fire Station 5 - 1803 Havendale Blvd., Winter Haven, FL 33881",
        "Contact": "Fire Station 1 - Non-Emergency Number - 863-291-5665\n\t\t       Fire Station 2 - Non-Emergency Number - 863-298-5212\n\t\t       Fire Station 3 - Non-Emergency Number - 863-298-5212\n\t\t       Fire Station 4 - Non-Emergency Number - 863-282-8034\n\t\t       Fire Station 5 - Non-Emergency Number - 863-282-8035",
    },
    
    "312": {
        "Department": "Parks & Grounds",
        "Location": "N/A:",
        "Contact": "N/A",

    },

    "700": {
        "Department": "Parks & Recreation Administration",
        "Location": "Nora Mayor Hall - 500 Third Street NW, Winter Haven, FL 33880",
        
    },

    "705": {
        "Department": "Fieldhouse & Conference Center",
        "Location": "AdventHealth FieldHouse & Conference Center - 210 Cypress Gardens Blvd, Winter Haven, FL 33880",
        "Contact": "N/A"
    }
}

windowsKeys = {
    "1": {
        "name": "Windows 11",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "2": {
        "name": "Windows 10",
        "key": "MVHNP-G8632-B482B-QDW8D-QRR8R"
    },
    "3": {
        "name": "Windows 8.1",
        "key": "MPXWC-7CN4B-64FCB-9T69B-F9BDQ"
    },
    "4": {
        "name": "Windows 7",
        "key": "YTH8H-3VJ37-T3RVT-YH7HG-KCVPD"
    },
    "5": {
        "name": "Microsoft Office 2024",
        "key": "GWNJM-H6FRF-39GGY-KHD9Y-MY883"
    }
}


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

#wait for keypress
def pause(msg="Press any key to continue..."):
    print(msg, end='', flush=True)
    if msvcrt:
        msvcrt.getch()
    else:
        # for some reason it wouldnt work without a fallback
        input()
    print()


def displayHome():
    clearScreen()
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


def displayMainMenu():
    #main menu options
    clearScreen()
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
    clearScreen()
    print("Cost Centers")
    print("=" * 12)
    for cc in costCenters:
        dept = costCenters[cc]["Department"]
        print(f"{cc}) {dept}")
    print("0) Back")
    choice = input("\nEnter cost center number: ").strip()
    return choice
def showCostCenter(ccNumber):
    clearScreen()
    data = costCenters.get(ccNumber)
    if not data:
        print("Invalid cost center number.")
        pause()
        return
    print(f"Cost Center: {ccNumber}")
    print("-" * 30)
    print(f"Department           : {data['Department']}\nLocation             : {data['Location']}\nPrimary Contact      : {data['Contact']}")
    print()
    pause()

def displayActivationKeyMenu():
    clearScreen()
    print("Windows Activation Keys")
    print("=" * 23)
    for k, v in windowsKeys.items():
        print(f"{k}) {v['name']}")
    print("0) Back")
    choice = input("\nSelect an option: ").strip()
    return choice

def showActivationKey(version):
    clearScreen()
    key_info = windowsKeys.get(version)
    if not key_info:
        print("Invalid selection.")
        pause()
        return
    print(f"{key_info['name']} Activation Key")
    print("=" * (len(key_info['name']) + 16))
    print(key_info['key'])
    if CLIPBOARD_AVAILABLE:
        pyperclip.copy(key_info['key'])
        print(f"\n[{key_info['name']} key has been copied to the clipboard.]\n")
    print()
    pause()

def main():
    displayHome()
    while True:
        choice = displayMainMenu()
        if choice == "1":
            while True:
                costCenterChoice = displayCostCenters()
                if costCenterChoice  == "0":
                    break
                showCostCenter(costCenterChoice)
        elif choice == "2":
            while True:
                version = displayActivationKeyMenu()
                if version == "0":
                    break
                showActivationKey(version)
        elif choice == "3":
            # Guides submenu
            while True:
                guideChoice = displayGuidesMenu()
                if guideChoice == "0":
                    break
                showGuide(guideChoice)
        elif choice == "4":
            # Troubleshooting submenu
            while True:
                troubleshootChoice = displayTroubleshootingMenu()
                if troubleshootChoice == "0":
                    break
                showTroubleshooting(troubleshootChoice)
        elif choice == "0":
            clearScreen()
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

